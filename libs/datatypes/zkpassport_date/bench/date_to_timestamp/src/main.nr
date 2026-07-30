use noir_date::Date;

fn main(year: u32, month: u8, day: u8) -> pub u64 {
    Date::new(year, month, day).to_timestamp()
}
