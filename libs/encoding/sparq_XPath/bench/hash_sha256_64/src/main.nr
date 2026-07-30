use xpath::sha256_hex;

fn main() -> pub [u8; 64] {
    let text: str<64> = "sparql xpath benchmark payload for sha256 hex output\0\0\0\0\0\0\0\0\0\0\0\0";
    let (hex, _) = sha256_hex(text);
    hex
}
