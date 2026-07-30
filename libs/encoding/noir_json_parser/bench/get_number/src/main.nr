use json_parser::JSON512b;

fn main() -> pub u64 {
    let text = "{ \"foo\": 1234, \"bar\": { \"foo\": 9876, \"bar\": true }, \"baz\": \"hello\" }";
    let json: JSON512b = JSON512b::parse_json_from_string(text);
    json.get_number_unchecked("foo".as_bytes())
}
