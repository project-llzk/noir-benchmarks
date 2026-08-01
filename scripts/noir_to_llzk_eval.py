#!/usr/bin/env python3

# Program: noir_to_llzk_eval.py
# Description: This script runs the noir -> acir -> llzk frontend
#   on noir-benchmarks and writes a CSV with timing results.
#
# Required Programs:
#   - python3 >= 3.11: For running this script
#   - nargo(>=1.0.0): For compiling benchmarks to acir
#   - acir2llzk: For compiling acir to llzk -> https://github.com/project-llzk/noir_llzk/
#
# Usage:
#   scripts/noir_to_llzk_eval.py \
#       [--nargo-bin PATH] \
#       [--a2l-bin PATH] \
#       [--benchmark_dir PATH] \
#       [--output-dir PATH] \
#       [--timeout SECONDS] \
#       [--nthreads N] \
#
# Example:
#   scripts/noir_to_llzk_eval.py --timeout 5 --nargo-bin ~/.nargo/bin/nargo --a2l-bin ~/gh/noir_llzk/target/release/acir2llzk
#
# The easiest appraoch is to run this script from the root of the `noir_llzk` repo within the nix dev shell:
#   [...]/noir-benchmarks/scripts/noir_to_llzk_eval.py --benchmark_dir [...]/noir-benchmarks --a2l-bin target/release/acir2llzk

import sys
if sys.version_info < (3, 11):
    sys.exit("error: noir_to_llzk_eval.py requires Python 3.11 or newer")

import argparse
import csv
import datetime
import glob
import json
import multiprocessing
import os
import shutil
import subprocess
import tempfile
import time
import tomllib
from typing import Dict, Iterable, List, Set, Tuple

Benchmark = Dict[str, str]
BenchmarkGroup = Dict[str, object]
Result = Tuple[str, str, str, str, str, str]

def benchmark_enabled(entry: Benchmark) -> bool:
    return entry.get("enabled") is True

def resolve_tool(binary: str) -> str:
    """Return an executable path for a configured binary, or raise FileNotFoundError."""
    expanded = os.path.expanduser(binary)
    if os.path.dirname(expanded):
        if os.path.isfile(expanded) and os.access(expanded, os.X_OK):
            return os.path.abspath(expanded)
        raise FileNotFoundError(f"Required executable not found or not executable: {binary}")

    resolved = shutil.which(expanded)
    if resolved:
        return resolved
    raise FileNotFoundError(f"Required executable not found on PATH: {binary}")

def load_benchmark_groups(benchmark_dir: str) -> List[BenchmarkGroup]:
    """Load benchmark metadata and expand workspaces into binary package benchmarks."""
    metadata_path = os.path.join(benchmark_dir, "benchmark_metadata.json")
    with open(metadata_path, "r", encoding="utf-8") as handle:
        metadata = json.load(handle)

    groups = []
    for entry in metadata:
        if not benchmark_enabled(entry):
            continue
        try:
            benchmark_name = entry["benchmark name"]
            benchmark_path = entry["path"]
        except KeyError as exc:
            raise ValueError(f"Invalid benchmark metadata entry, missing {exc}") from exc
        benchmark_path = os.path.abspath(os.path.join(benchmark_dir, benchmark_path))
        nargo_toml = os.path.join(benchmark_path, "Nargo.toml")
        manifest = _load_nargo_manifest(nargo_toml)
        workspace = manifest.get("workspace")

        required_paths, missing_dependencies = _collect_required_nargo_paths(benchmark_path, manifest)

        if workspace:
            benchmarks = []
            for member in workspace.get("members", []):
                member_path = os.path.abspath(os.path.join(benchmark_path, member))
                member_manifest = _load_nargo_manifest(os.path.join(member_path, "Nargo.toml"))
                if _package_type(member_manifest) != "bin":
                    continue
                package_name = _package_name(member_manifest, member_path)
                benchmarks.append({
                    "name": f"{benchmark_name}/{package_name}",
                    "json_name": package_name,
                    "output_stem": os.path.join(benchmark_name, package_name),
                })
            groups.append({
                "name": benchmark_name,
                "source_path": benchmark_path,
                "compile_args": ["compile", "--workspace"],
                "required_paths": required_paths,
                "missing_dependencies": missing_dependencies,
                "benchmarks": benchmarks,
            })
        else:
            package_name = _package_name(manifest, benchmark_path)
            groups.append({
                "name": benchmark_name,
                "source_path": benchmark_path,
                "compile_args": ["compile"],
                "required_paths": required_paths,
                "missing_dependencies": missing_dependencies,
                "benchmarks": [{
                    "name": benchmark_name,
                    "json_name": package_name,
                    "output_stem": benchmark_name,
                }],
            })
    return sorted(groups, key=lambda group: str(group["name"]))

def _load_nargo_manifest(nargo_toml: str) -> Dict:
    with open(nargo_toml, "rb") as handle:
        return tomllib.load(handle)

def _package_name(manifest: Dict, package_path: str) -> str:
    package = manifest.get("package", {})
    return package.get("name") or os.path.basename(os.path.normpath(package_path))

def _package_type(manifest: Dict) -> str:
    package = manifest.get("package", {})
    return package.get("type", "bin")

def _collect_required_nargo_paths(root_path: str, root_manifest: Dict) -> Tuple[List[str], List[str]]:
    """Return Nargo project paths needed to compile root_path plus missing manifests."""
    required_paths: Set[str] = {root_path}
    missing_dependencies: Set[str] = set()
    visited: Set[str] = set()

    workspace = root_manifest.get("workspace")
    if workspace:
        pending = [
            os.path.abspath(os.path.join(root_path, member))
            for member in workspace.get("members", [])
        ]
    else:
        pending = [root_path]

    while pending:
        package_path = os.path.abspath(pending.pop())
        if package_path in visited:
            continue
        visited.add(package_path)
        required_paths.add(package_path)

        manifest_path = os.path.join(package_path, "Nargo.toml")
        if package_path == root_path:
            manifest = root_manifest
        elif os.path.isfile(manifest_path):
            manifest = _load_nargo_manifest(manifest_path)
        else:
            missing_dependencies.add(manifest_path)
            continue

        for dependency_path in _local_dependency_paths(manifest, package_path):
            dependency_manifest = os.path.join(dependency_path, "Nargo.toml")
            if os.path.isfile(dependency_manifest):
                pending.append(dependency_path)
            else:
                missing_dependencies.add(dependency_manifest)

    return sorted(required_paths), sorted(missing_dependencies)

def _local_dependency_paths(manifest: Dict, manifest_dir: str) -> Iterable[str]:
    for section_name in ("dependencies", "dev-dependencies"):
        dependencies = manifest.get(section_name, {})
        if not isinstance(dependencies, dict):
            continue
        for dependency in dependencies.values():
            if not isinstance(dependency, dict):
                continue
            dependency_path = dependency.get("path")
            if isinstance(dependency_path, str):
                yield os.path.abspath(os.path.join(manifest_dir, dependency_path))

def _error_message(stage: str, message: str) -> str:
    return f"{stage}: {message.strip()[:400]}"

def _subprocess_error(stage: str, proc: subprocess.CompletedProcess) -> str:
    message = (proc.stderr or proc.stdout or "").strip()
    if not message:
        message = f"exit code {proc.returncode}"
    return _error_message(stage, message)

def _timeout_arg(timeout: float):
    return timeout if timeout is not None and timeout > 0 else None

def _find_compiled_json(benchmark_path: str, json_name: str) -> str:
    exact_candidates = [
        os.path.join(benchmark_path, f"{json_name}.json"),
        os.path.join(benchmark_path, "target", f"{json_name}.json"),
    ]
    for candidate in exact_candidates:
        if os.path.isfile(candidate):
            return candidate

    json_candidates = [
        candidate
        for pattern in (
            os.path.join(benchmark_path, "target", "*.json"),
            os.path.join(benchmark_path, "*.json"),
        )
        for candidate in glob.glob(pattern)
    ]
    if len(json_candidates) == 1:
        return json_candidates[0]
    if not json_candidates:
        raise FileNotFoundError(f"nargo did not produce {json_name}.json")
    raise FileNotFoundError(
        f"nargo produced multiple JSON files, but none named {json_name}.json"
    )

def _is_relative_to(path: str, parent: str) -> bool:
    return os.path.commonpath([path, parent]) == parent

def _minimal_copy_roots(paths: List[str]) -> List[str]:
    copy_roots = []
    for path in sorted(set(os.path.abspath(path) for path in paths)):
        if any(_is_relative_to(path, existing) for existing in copy_roots):
            continue
        copy_roots = [
            existing
            for existing in copy_roots
            if not _is_relative_to(existing, path)
        ]
        copy_roots.append(path)
    return copy_roots

def _copy_benchmark_source(
    source_path: str,
    work_dir: str,
    required_paths: List[str] | None = None,
) -> str:
    copy_root = source_path
    benchmark_relpath = "."
    bench_dir = os.path.dirname(source_path)
    primary_dir = os.path.dirname(bench_dir)
    if (
        os.path.basename(bench_dir) == "bench"
        and os.path.isfile(os.path.join(primary_dir, "lib", "Nargo.toml"))
    ):
        copy_root = primary_dir
        benchmark_relpath = os.path.relpath(source_path, copy_root)

    destination = os.path.join(work_dir, "benchmark")
    paths_to_copy = _minimal_copy_roots([copy_root, *(required_paths or [])])
    common_root = os.path.commonpath(paths_to_copy)

    if len(paths_to_copy) == 1 and paths_to_copy[0] == common_root:
        selected_root = paths_to_copy[0]
        shutil.copytree(
            selected_root,
            destination,
            ignore=shutil.ignore_patterns("target", "llzk-outputs"),
            symlinks=True,
        )
        benchmark_relpath = os.path.relpath(source_path, selected_root)
    else:
        os.makedirs(destination, exist_ok=True)
        for path in paths_to_copy:
            relative_path = os.path.relpath(path, common_root)
            destination_path = os.path.join(destination, relative_path)
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copytree(
                path,
                destination_path,
                ignore=shutil.ignore_patterns("target", "llzk-outputs"),
                symlinks=True,
            )
        benchmark_relpath = os.path.relpath(source_path, common_root)

    return os.path.join(destination, benchmark_relpath)

def _missing_dependencies_error(missing_dependencies: List[str]) -> str:
    display_paths = []
    for path in missing_dependencies:
        try:
            display_paths.append(os.path.relpath(path))
        except ValueError:
            display_paths.append(path)
    missing_list = ", ".join(display_paths[:8])
    remaining = len(display_paths) - 8
    if remaining > 0:
        missing_list = f"{missing_list}, and {remaining} more"
    return f"missing local path dependency manifests in source checkout: {missing_list}"

def _remove_if_exists(path: str) -> None:
    try:
        os.unlink(path)
    except FileNotFoundError:
        pass

def _output_paths(output_dir: str, benchmark: Benchmark) -> Tuple[str, str]:
    acir_json = os.path.join(output_dir, f"{benchmark['output_stem']}.json")
    llzk_output = os.path.join(output_dir, f"{benchmark['output_stem']}.llzk")
    os.makedirs(os.path.dirname(acir_json), exist_ok=True)
    return acir_json, llzk_output

def _result(
    benchmark_name: str,
    result: str,
    nargo_time: float,
    a2l_time: float,
    error_message: str,
) -> Result:
    return (
        benchmark_name,
        result,
        f"{nargo_time:.6f}",
        f"{a2l_time:.6f}",
        f"{nargo_time + a2l_time:.6f}",
        error_message,
    )

def _convert_benchmark(
    benchmark: Benchmark,
    benchmark_path: str,
    output_dir: str,
    a2l_bin: str,
    timeout: float,
    nargo_time: float,
) -> Result:
    benchmark_name = benchmark["name"]
    acir_json, llzk_output = _output_paths(output_dir, benchmark)
    _remove_if_exists(acir_json)
    _remove_if_exists(llzk_output)
    llzk_tmp = None
    try:
        compiled_json = _find_compiled_json(benchmark_path, benchmark["json_name"])
        shutil.copy2(compiled_json, acir_json)

        a2l_start = time.perf_counter()
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=os.path.dirname(llzk_output),
            prefix=f".{os.path.basename(llzk_output)}.",
            delete=False,
        ) as handle:
            llzk_tmp = handle.name
            convert_proc = subprocess.run(
                [a2l_bin, acir_json],
                stdout=handle,
                stderr=subprocess.PIPE,
                text=True,
                timeout=_timeout_arg(timeout),
            )
        a2l_time = time.perf_counter() - a2l_start
        if convert_proc.returncode == 0:
            shutil.move(llzk_tmp, llzk_output)
            return _result(benchmark_name, "success", nargo_time, a2l_time, "")
        _remove_if_exists(llzk_tmp)
        return _result(benchmark_name, "error", nargo_time, a2l_time, _subprocess_error("acir2llzk", convert_proc))
    except FileNotFoundError as exc:
        return _result(benchmark_name, "error", nargo_time, 0.0, _error_message("setup", str(exc)))
    except subprocess.TimeoutExpired:
        _remove_if_exists(llzk_tmp)
        a2l_time = time.perf_counter() - a2l_start
        return _result(benchmark_name, "timeout", nargo_time, a2l_time, "acir2llzk timeout")

def _run_group_unpack(packed: Tuple) -> List[Result]:
    return run_group(*packed)

def run_group(
    group: BenchmarkGroup,
    nargo_bin: str,
    a2l_bin: str,
    output_dir: str,
    timeout: float,
) -> List[Result]:
    group_name = str(group["name"])
    source_path = str(group["source_path"])
    benchmarks = group["benchmarks"]
    required_paths = group.get("required_paths", [])
    missing_dependencies = group.get("missing_dependencies", [])
    compile_start = None
    if not isinstance(benchmarks, list):
        raise TypeError(f"Invalid benchmarks list for {group_name}")
    if not isinstance(required_paths, list):
        raise TypeError(f"Invalid required paths list for {group_name}")
    if not isinstance(missing_dependencies, list):
        raise TypeError(f"Invalid missing dependencies list for {group_name}")

    try:
        if not os.path.isdir(source_path):
            raise FileNotFoundError(f"benchmark path does not exist: {source_path}")
        if not os.path.isfile(os.path.join(source_path, "Nargo.toml")):
            raise FileNotFoundError(f"benchmark path does not contain Nargo.toml: {source_path}")
        if missing_dependencies:
            raise FileNotFoundError(_missing_dependencies_error(missing_dependencies))

        with tempfile.TemporaryDirectory(prefix="nargo-", dir=output_dir) as work_dir:
            benchmark_path = _copy_benchmark_source(source_path, work_dir, required_paths)
            compile_start = time.perf_counter()
            compile_proc = subprocess.run(
                [nargo_bin, *group["compile_args"]],
                cwd=benchmark_path,
                capture_output=True,
                text=True,
                timeout=_timeout_arg(timeout),
            )
            nargo_time = time.perf_counter() - compile_start
            if compile_proc.returncode != 0:
                error = _subprocess_error("nargo compile", compile_proc)
                return [
                    _result(benchmark["name"], "error", nargo_time, 0.0, error)
                    for benchmark in benchmarks
                ]

            return [
                _convert_benchmark(benchmark, benchmark_path, output_dir, a2l_bin, timeout, nargo_time)
                for benchmark in benchmarks
            ]
    except FileNotFoundError as exc:
        error = _error_message("setup", str(exc))
        return [
            _result(benchmark["name"], "error", 0.0, 0.0, error)
            for benchmark in benchmarks
        ]
    except subprocess.TimeoutExpired:
        nargo_time = time.perf_counter() - compile_start if compile_start is not None else 0.0
        return [
            _result(benchmark["name"], "timeout", nargo_time, 0.0, "nargo compile timeout")
            for benchmark in benchmarks
        ]

def run_benchmarks(
    groups: List[BenchmarkGroup],
    timeout: float,
    nargo_bin: str,
    a2l_bin: str,
    output_dir: str,
    nthreads: int,
):
    """Run noir->llzk on benchmarks and save timing/error results to a CSV."""
    results = []
    success_cnt = 0
    error_cnt = 0
    timeout_cnt = 0

    os.makedirs(output_dir, exist_ok=True)
    group_args = [
        (group, nargo_bin, a2l_bin, output_dir, timeout)
        for group in groups
    ]

    if nthreads == 1:
        for group, group_nargo_bin, group_a2l_bin, group_output_dir, group_timeout in group_args:
            print(f"Running {group['name']}")
            group_results = run_group(
                group,
                group_nargo_bin,
                group_a2l_bin,
                group_output_dir,
                group_timeout,
            )
            results.extend(group_results)
            print(f"Exit conditions: {', '.join(result[1] for result in group_results)}")
    else:
        total = len(group_args)
        print(f"Launching {total} benchmark compile groups.")
        next_milestone = 10
        with multiprocessing.Pool(nthreads) as p:
            for i, group_results in enumerate(p.imap_unordered(_run_group_unpack, group_args), start=1):
                results.extend(group_results)
                pct = i * 100 // total
                if pct >= next_milestone:
                    print(f"Progress: {i}/{total} ({pct}%) compile groups complete")
                    next_milestone += 10

    results.sort()
    for _, cause, _, _, _, _ in results:
        success_cnt += 1 if cause == "success" else 0
        error_cnt += 1 if cause == "error" else 0
        timeout_cnt += 1 if cause == "timeout" else 0

    output_path = os.path.join(output_dir, "benchmarks_results.csv")
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "Benchmark",
            "Result",
            "Nargo Compile Time (sec)",
            "ACIR2LLZK Time (sec)",
            "Total Time (sec)",
            "Error Message",
        ])
        writer.writerows(results)
    print(f"success: {success_cnt}, errored: {error_cnt}, timeout: {timeout_cnt}")
    return output_path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Run noir benchmarks and collect timing results.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--benchmark_dir", default=".", help="Path to the noir-benchmarks directory.")
    parser.add_argument("--output-dir", default="llzk-outputs", help="Directory for generated ACIR, LLZK, and CSV output.")
    parser.add_argument("--timeout", type=float, default=10, help="Per-benchmark timeout in seconds.")
    parser.add_argument("--nargo-bin", default="nargo", help="Path to the nargo binary.")
    parser.add_argument("--a2l-bin", default="acir2llzk", help="Path to the acir2llzk binary.")
    parser.add_argument("--nthreads", type=int, default=os.cpu_count() or 1, help="Number of compile groups to run at once.")
    args = parser.parse_args()
    start = time.time()
    benchmark_dir = os.path.abspath(args.benchmark_dir)
    output_dir = args.output_dir
    if not os.path.isabs(output_dir):
        output_dir = os.path.join(benchmark_dir, output_dir)
    output_dir = os.path.abspath(output_dir)
    print(f"{benchmark_dir = }")
    print(f"{output_dir = }")
    try:
        nargo_bin = resolve_tool(args.nargo_bin)
        a2l_bin = resolve_tool(args.a2l_bin)
    except FileNotFoundError as exc:
        parser.error(str(exc))
    groups = load_benchmark_groups(benchmark_dir)
    run_benchmarks(
        groups,
        args.timeout,
        nargo_bin,
        a2l_bin,
        output_dir,
        args.nthreads
    )
    elapsed = datetime.timedelta(seconds=time.time() - start)
    print(f"Total benchmark execution time: {elapsed}")
