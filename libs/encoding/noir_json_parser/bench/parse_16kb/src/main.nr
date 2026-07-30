use json_parser::JSON16kb;

fn main(input: [u8; 16384]) -> pub u32 {
    let json: JSON16kb = JSON16kb::parse_json(input);
    json.get_length()
}
