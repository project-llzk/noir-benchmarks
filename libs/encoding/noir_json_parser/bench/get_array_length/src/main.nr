use json_parser::JSON512b;

fn main() -> pub u32 {
    let text = "{ \"foo\": [ [1,2,3], [[3,4]], [[]], [], { \"bar\": [\"b\", \"a\", \"z\" ]} ]}";
    let json: JSON512b = JSON512b::parse_json_from_string(text);
    let first = json.get_array_unchecked("foo".as_bytes());
    first.get_length()
}
