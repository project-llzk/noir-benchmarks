use xpath::replace_literal;

fn main() -> pub [u8; 32] {
    let text: str<32> = "alpha.beta.gamma.delta.epsilon\0\0";
    let pattern: str<1> = ".";
    let replacement: str<1> = "/";
    let (out, _) = replace_literal::<32, 1, 1, 32>(text, pattern, replacement);
    out
}
