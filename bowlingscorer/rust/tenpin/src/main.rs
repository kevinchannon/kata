mod tenpin;

use std::io;

fn main() {
    println!("Enter pins knocked down in each frame:");

    let mut pins_knocked_down = String::new();

    io::stdin().read_line(&mut pins_knocked_down).expect("Failed to read pins knocked down");

    println!("Game score = {}", tenpin::score(pins_knocked_down.trim().to_string()));
}
