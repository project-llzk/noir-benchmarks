use bignum::{BigNum, BN254_Fq};

fn main(seed: [u8; 13]) -> pub BN254_Fq {
    BN254_Fq::derive_from_seed(seed)
}
