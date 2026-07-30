use noir_base64::BASE64_ENCODER;

fn main(input: BoundedVec<u8, 610>) -> pub BoundedVec<u8, 816> {
    BASE64_ENCODER::encode_var(input)
}
