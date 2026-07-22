use noir_bigcurve::{BigCurve, BN254, BN254Scalar};

fn main(point: BN254, scalar: Field) -> pub BN254 {
    let scalar: BN254Scalar = BN254Scalar::from(scalar);
    point.mul(scalar)
}
