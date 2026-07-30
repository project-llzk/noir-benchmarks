use json_parser::JSON512b;

fn main(input: [u8; 512]) -> pub u32 {
    let json: JSON512b = JSON512b::parse_json(input);
    json.get_length()
}
