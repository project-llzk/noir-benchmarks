use noir_bigcurve::{BigCurve, BN254};

fn main(point: BN254) {
    point.validate_on_curve();
}
