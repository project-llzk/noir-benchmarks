use keccak256::keccak256;

fn main(input: [u8; 100], len: u32) -> pub [u8; 32] {
    keccak256(input, len)
}
