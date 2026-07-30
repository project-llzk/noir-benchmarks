use json_parser::JSON8kb;

fn main(input: [u8; 8192]) -> pub u32 {
    let json: JSON8kb = JSON8kb::parse_json(input);
    json.get_length()
}
