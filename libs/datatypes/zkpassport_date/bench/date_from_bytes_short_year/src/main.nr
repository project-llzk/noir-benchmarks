use noir_date::Date;

fn main(date: [u8; 6], threshold_year: u32, threshold_month: u8, threshold_day: u8) -> pub [u8; 8] {
    let threshold_date = Date::new(threshold_year, threshold_month, threshold_day);
    Date::from_bytes_short_year(date, threshold_date).to_bytes()
}
