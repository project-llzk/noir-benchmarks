use noir_base64::BASE64_ENCODER;

fn main(input: [u8; 610]) -> pub [u8; 816] {
    BASE64_ENCODER::encode(input)
}
