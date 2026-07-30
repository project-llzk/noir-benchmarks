use wad_lib::wad_mul_div;

fn main(value: Field, other: Field, divisor: Field) -> pub Field {
    wad_mul_div(value, other, divisor)
}
