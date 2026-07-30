use sparq_ieee754::f16;

fn main(a: u16, b: u16) -> pub u16 {
    (f16::new(a) * f16::new(b)).bits()
}
