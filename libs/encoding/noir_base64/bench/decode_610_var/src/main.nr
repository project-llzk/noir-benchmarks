use noir_base64::BASE64_DECODER;

fn main(input: BoundedVec<u8, 816>) -> pub BoundedVec<u8, 610> {
    let r = BASE64_DECODER::decode_var(input);
    r
}
