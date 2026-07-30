use noir_base64::BASE64_DECODER;

fn main(input: [u8; 816]) -> pub [u8; 610] {
    BASE64_DECODER::decode(input)
}
