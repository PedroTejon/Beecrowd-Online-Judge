use std::io::{stdin};

fn main() {
    let mut num1 = String::new();    
    stdin().read_line(&mut num1).expect("Erro");
    
    let num1: f64 = match num1.trim().parse() {
        Ok(num) => num,
        Err(_) => 0.0
    };
    
    println!("A={:.4}", 3.14159 * (num1 * num1));
}