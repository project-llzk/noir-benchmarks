use sparq_ieee754::f16;

fn main(a: u16, b: u16) -> pub bool {
    f16::new(a).lt(f16::new(b))
}
