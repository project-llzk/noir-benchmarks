use noir_string_search::{StringBody, StringBody32, SubString, SubString32};

fn main(haystack_input: [u8; 32], haystack_len: u32, needle_input: [u8; 32], needle_len: u32) -> pub u32 {
    let haystack: StringBody32 = StringBody::new(haystack_input, haystack_len);
    let needle: SubString32 = SubString::new(needle_input, needle_len);
    let (result, position) = haystack.substring_match(needle);
    assert(result);
    position
}
