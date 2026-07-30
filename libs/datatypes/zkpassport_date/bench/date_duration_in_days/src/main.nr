use noir_date::Date;

fn main(
    year: u32,
    month: u8,
    day: u8,
    other_year: u32,
    other_month: u8,
    other_day: u8,
    absolute: bool,
) -> pub i64 {
    let date = Date::new(year, month, day);
    let other = Date::new(other_year, other_month, other_day);
    date.get_duration_in_days(other, absolute)
}
