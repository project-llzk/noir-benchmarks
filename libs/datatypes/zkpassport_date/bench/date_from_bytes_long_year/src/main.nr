use noir_date::Date;

fn main(date: [u8; 8]) -> pub [u8; 8] {
    Date::from_bytes_long_year(date).to_bytes()
}
