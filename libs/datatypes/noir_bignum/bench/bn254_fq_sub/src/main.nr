use bignum::BN254_Fq;

fn main(a: BN254_Fq, b: BN254_Fq) -> pub BN254_Fq {
    a - b
}
