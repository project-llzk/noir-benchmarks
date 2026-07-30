use noir_base64::BASE64_URL_ENCODER;

fn main(input: [u8; 610]) -> pub [u8; 814] {
    BASE64_URL_ENCODER::encode(input)
}
