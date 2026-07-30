use bignum::{BigNum, BN254_Fq};

fn main(value: BN254_Fq) -> pub [u8; 32] {
    value.to_be_bytes()
}
