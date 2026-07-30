use sha256::sha256_var;

fn main(input: [u8; 511], len: u32) -> pub [u8; 32] {
    sha256_var(input, len)
}
