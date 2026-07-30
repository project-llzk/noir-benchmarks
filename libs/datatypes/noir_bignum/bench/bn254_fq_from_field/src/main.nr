use bignum::BN254_Fq;

fn main(value: Field) -> pub BN254_Fq {
    BN254_Fq::from(value)
}
