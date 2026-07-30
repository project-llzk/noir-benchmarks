use sha512::sha512;

fn main(input: [u8; 111]) -> pub [u8; 64] {
    sha512::digest(input)
}
