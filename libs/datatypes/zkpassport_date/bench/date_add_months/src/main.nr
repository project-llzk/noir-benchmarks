use noir_date::Date;

fn main(year: u32, month: u8, day: u8, months: u32) -> pub [u8; 8] {
    Date::new(year, month, day).add_months(months).to_bytes()
}
