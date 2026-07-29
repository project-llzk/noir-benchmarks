use mimc::mimc_bn254;

fn main(input: [Field; 10]) -> pub Field {
    mimc_bn254(input)
}
