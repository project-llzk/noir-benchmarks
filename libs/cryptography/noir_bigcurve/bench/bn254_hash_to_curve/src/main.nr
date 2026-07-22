use noir_bigcurve::{BigCurve, BN254};

fn main(seed: [u8; 10]) -> pub BN254 {
    BN254::hash_to_curve(seed)
}
