use xpath::JSON512b;

fn main(input: [u8; 512], index: Field) -> pub u64 {
    let json: JSON512b = JSON512b::parse_json(input);
    json.get_number_from_array_unchecked(index)
}
