use noir_string_search::{StringBody, StringBody512, SubString, SubString64};

fn main(haystack_input: [u8; 512], haystack_len: u32, needle_input: [u8; 64], needle_len: u32) -> pub u32 {
    let haystack: StringBody512 = StringBody::new(haystack_input, haystack_len);
    let needle: SubString64 = SubString::new(needle_input, needle_len);
    let (result, position) = haystack.substring_match(needle);
    assert(result);
    position
}
