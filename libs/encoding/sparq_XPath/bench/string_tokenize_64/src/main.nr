use xpath::tokenize_whitespace;

fn main() -> pub u32 {
    let text: str<64> = "alpha beta  gamma delta epsilon zeta eta theta iota\0\0\0\0\0\0\0\0\0\0\0\0\0";
    let (_, _, count) = tokenize_whitespace::<64, 10, 12>(text);
    count
}
