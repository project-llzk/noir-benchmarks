use bignum::{BigNum, BN254_Fq};

fn main(bytes: [u8; 32]) -> pub BN254_Fq {
    BN254_Fq::from_be_bytes(bytes)
}
