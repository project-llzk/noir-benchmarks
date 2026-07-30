use sparq_ieee754::f64;

fn main(value: u64) -> pub u64 {
    f64::new(value).sqrt().bits()
}
