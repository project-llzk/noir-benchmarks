use noir_base64::BASE64_URL_ENCODER;

fn main(input: BoundedVec<u8, 610>) -> pub BoundedVec<u8, 814> {
    BASE64_URL_ENCODER::encode_var(input)
}
