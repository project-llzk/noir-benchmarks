use sparq_ieee754::f32;

fn main(a: u32, b: u32) -> pub u32 {
    (f32::new(a) / f32::new(b)).bits()
}
