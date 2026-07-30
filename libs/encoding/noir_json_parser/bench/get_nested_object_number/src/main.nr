use json_parser::JSON512b;

fn main() -> pub u64 {
    let text = "{ \"foo\": 1234, \"bar\": { \"foo\": 9876, \"bar\": true }, \"baz\": \"hello\" }";
    let json: JSON512b = JSON512b::parse_json_from_string(text);
    let nested_json = json.get_object_unchecked("bar".as_bytes());
    nested_json.get_number_unchecked("foo".as_bytes())
}
