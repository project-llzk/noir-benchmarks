use bignum::U256;
use bignum::bignum::evaluate_quadratic_expression;

fn main(
    lhs: [[U256; 1]; 3],
    lhs_flags: [[bool; 1]; 3],
    rhs: [[U256; 1]; 3],
    rhs_flags: [[bool; 1]; 3],
    add: [U256; 3],
    add_flags: [bool; 3],
) {
    evaluate_quadratic_expression(lhs, lhs_flags, rhs, rhs_flags, add, add_flags)
}
