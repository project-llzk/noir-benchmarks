use json_parser::JSON512b;

fn main() -> pub [u8; 5] {
    let text = "{ \"foo\": 1234, \"bar\": { \"foo\": 9876, \"bar\": true }, \"baz\": \"hello\" }";
    let json: JSON512b = JSON512b::parse_json_from_string(text);
    let result: BoundedVec<u8, 5> = json.get_string_unchecked("baz".as_bytes());
    result.storage()
}
