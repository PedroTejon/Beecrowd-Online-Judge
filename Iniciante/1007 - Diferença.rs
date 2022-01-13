use std::io::{stdin};

fn main() {
    let mut num1 = String::new();    
    let mut num2 = String::new();
    let mut num3 = String::new();
    let mut num4 = String::new();
    
    stdin().read_line(&mut num1).expect("Erro");
    stdin().read_line(&mut num2).expect("Erro");
    stdin().read_line(&mut num3).expect("Erro");
    stdin().read_line(&mut num4).expect("Erro");
    
    let num1: i32 = num1.trim().parse().expect("Erro");
    let num2: i32 = num2.trim().parse().expect("Erro");
    let num3: i32 = num3.trim().parse().expect("Erro");
    let num4: i32 = num4.trim().parse().expect("Erro");
    
    println!("DIFERENCA = {}", (num1 * num2) - (num3 * num4));
}