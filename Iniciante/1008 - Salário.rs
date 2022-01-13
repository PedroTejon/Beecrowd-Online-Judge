use std::io::{stdin};

fn main() {
    let mut num1 = String::new();
    let mut num2 = String::new();
    let mut num3 = String::new();
    
    stdin().read_line(&mut num1).expect("Erro");
    stdin().read_line(&mut num2).expect("Erro");
    stdin().read_line(&mut num3).expect("Erro");
    
    let num1: i32 = num1.trim().parse().expect("Erro");
    let num2: i32 = num2.trim().parse().expect("Erro");
    let num3: f32 = num3.trim().parse().expect("Erro");
    
    println!("NUMBER = {}\nSALARY = U$ {:.2}", num1, num2 as f32 * num3);
}