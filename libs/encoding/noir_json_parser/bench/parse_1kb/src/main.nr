use json_parser::JSON1kb;

fn main(input: [u8; 1024]) -> pub u32 {
    let json: JSON1kb = JSON1kb::parse_json(input);
    json.get_length()
}
