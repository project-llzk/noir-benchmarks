use json_parser::JSON4kb;

fn main(input: [u8; 4096]) -> pub u32 {
    let json: JSON4kb = JSON4kb::parse_json(input);
    json.get_length()
}
