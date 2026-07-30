use mimc::mimc_bn254;

fn main(input: [Field; 100]) -> pub Field {
    mimc_bn254(input)
}
