use noir_date::Date;

fn main(timestamp: u64) -> pub [u8; 8] {
    Date::from_timestamp(timestamp).to_bytes()
}
