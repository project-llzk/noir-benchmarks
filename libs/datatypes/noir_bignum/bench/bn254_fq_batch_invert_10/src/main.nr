use bignum::BN254_Fq;
use bignum::bignum::batch_invert;

fn main(values: [BN254_Fq; 10]) -> pub [BN254_Fq; 10] {
    // Safety:
    unsafe { batch_invert(values) }
}
