use xpath::sort_int;

fn main(values: [i64; 32], len: u32) -> pub [i64; 32] {
    assert(len <= 32);
    sort_int(values, len)
}
