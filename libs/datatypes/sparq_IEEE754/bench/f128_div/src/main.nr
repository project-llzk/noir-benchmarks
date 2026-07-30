use sparq_ieee754::f128;

fn main(a: u128, b: u128) -> pub u128 {
    (f128::new(a) / f128::new(b)).bits()
}
