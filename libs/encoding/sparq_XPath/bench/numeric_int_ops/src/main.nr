use xpath::{
    abs_int, max_int, min_int, numeric_add_int, numeric_divide_int, numeric_mod_int,
    numeric_multiply_int, numeric_subtract_int,
};

fn main(a: i64, b: i64) -> pub i64 {
    assert(b != 0);
    let sum = numeric_add_int(a, b);
    let diff = numeric_subtract_int(a, b);
    let product = numeric_multiply_int(a, b);
    let quotient = numeric_divide_int(a, b);
    let remainder = numeric_mod_int(a, b);
    let low = min_int(a, b);
    let high = max_int(a, b);
    abs_int(sum + diff + product + quotient + remainder + low + high)
}
