use xpath::{date_add_duration, date_from_components, duration_from_microseconds};

fn main(year: i32, month: u8, day: u8, micros: i64) -> pub i32 {
    let date = date_from_components(year, month, day);
    let duration = duration_from_microseconds(micros);
    let result = date_add_duration(date, duration);
    result.epoch_days
}
