use sparq_ieee754::f32;

fn main(value: u32) -> pub u32 {
    f32::new(value).round_ties_even().bits()
}
