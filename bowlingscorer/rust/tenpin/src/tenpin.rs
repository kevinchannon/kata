pub fn score(_pins_knocked_down: String) -> u16 {
    300
}

#[cfg(test)]
mod test {
use super::*;

    #[test]
    fn twenty_gutter_balls_returns_zero() {
        assert_eq!(0, score("00 00 00 00 00 00 00 00 00 00".to_string()));
    }
}