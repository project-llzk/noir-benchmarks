# Noir → LLZK Benchmarks

This repository is a benchmark set for converting Noir programs to LLZK.

The LLZK backend for Noir can be found here:

```
https://github.com/project-llzk/noir_llzk
```

The list of benchmarks is recorded in `benchmark_metadata.json`. It is organized into two top-level categories:

- `applications/`: Noir applications and end-to-end circuits.
- `libs/`: Common and popular Noir libraries used by applications.

## Running LLZK Over Benchmarks

Use Python 3.11 or newer to run the evaluation script with the `noir_llzk` binary:

```
python3 noir_to_llzk_eval.py --benchmark_dir . --timeout [seconds] --noir-bin [path-to-noir-bin]
```
