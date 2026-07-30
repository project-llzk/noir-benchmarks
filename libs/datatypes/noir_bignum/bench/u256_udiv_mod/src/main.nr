use bignum::{BigNum, U256};

fn main(a: U256, b: U256) -> pub (U256, U256) {
    a.udiv_mod(b)
}
