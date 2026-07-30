use sparq_ieee754::f64;

fn main(value: u64) -> pub i64 {
    f64::new(value).to_i64()
}
