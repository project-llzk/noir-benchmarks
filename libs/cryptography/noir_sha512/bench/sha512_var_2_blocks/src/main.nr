use sha512::sha512;

fn main(input: BoundedVec<u8, 239>) -> pub [u8; 64] {
    sha512::sha512_var(input)
}
