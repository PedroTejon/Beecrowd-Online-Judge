use std::io::{stdin};

fn main() {
    let mut num1 = String::new();    
    let mut num2 = String::new();
    stdin().read_line(&mut num1).expect("Erro");
    stdin().read_line(&mut num2).expect("Erro");
    
    let num1: f32 = match num1.trim().parse() {
        Ok(num) => num,
        Err(_) => 0.0
    };
    let num2: f32 = match num2.trim().parse() {
        Ok(num) => num,
        Err(_) => 0.0
    };
    
    
    println!("MEDIA = {:.5}", (num1 * 3.5 + num2 * 7.5) / 11.0);
}