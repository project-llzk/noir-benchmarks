use noir_bigcurve::{BigCurve, BN254, BN254Scalar};

fn main(mul_points: [BN254; 2], scalars: [Field; 2], add_point: BN254) -> pub BN254 {
    let scalar_0: BN254Scalar = BN254Scalar::from(scalars[0]);
    let scalar_1: BN254Scalar = BN254Scalar::from(scalars[1]);

    BN254::evaluate_linear_expression(mul_points, [scalar_0, scalar_1], [add_point])
}
