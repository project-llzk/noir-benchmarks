use xpath::contains;

fn main() -> pub bool {
    let text: str<64> = "the quick brown fox jumps over the lazy dog near the riverbank\0\0";
    let needle: str<8> = "river\0\0\0";
    contains(text, needle)
}
