use keccak256::keccak256;

fn main(input: [u8; 135], len: u32) -> pub [u8; 32] {
    keccak256(input, len)
}
