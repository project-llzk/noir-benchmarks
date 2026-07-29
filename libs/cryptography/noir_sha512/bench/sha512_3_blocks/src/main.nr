use sha512::sha512;

fn main(input: [u8; 367]) -> pub [u8; 64] {
    sha512::digest(input)
}
