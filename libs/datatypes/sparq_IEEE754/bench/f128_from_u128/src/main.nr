use sparq_ieee754::f128;

fn main(value: u128) -> pub u128 {
    f128::from(value).bits()
}
