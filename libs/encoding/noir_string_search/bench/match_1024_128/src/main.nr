use noir_string_search::{StringBody, StringBody1024, SubString, SubString128};

fn main(haystack_input: [u8; 1024], haystack_len: u32, needle_input: [u8; 128], needle_len: u32) -> pub u32 {
    let haystack: StringBody1024 = StringBody::new(haystack_input, haystack_len);
    let needle: SubString128 = SubString::new(needle_input, needle_len);
    let (result, position) = haystack.substring_match(needle);
    assert(result);
    position
}
