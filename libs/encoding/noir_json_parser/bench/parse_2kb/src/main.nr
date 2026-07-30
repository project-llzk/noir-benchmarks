use json_parser::JSON2kb;

fn main(input: [u8; 2048]) -> pub u32 {
    let json: JSON2kb = JSON2kb::parse_json(input);
    json.get_length()
}
