use std::io::{stdin};

fn main() {
    let mut num1 = String::new();    
    let mut num2 = String::new();
    let mut num3 = String::new();
    
    stdin().read_line(&mut num1).expect("Erro");
    stdin().read_line(&mut num2).expect("Erro");
    stdin().read_line(&mut num3).expect("Erro");
    
    let num2: f64 = num2.trim().parse().expect("Erro");
    let num3: f64 = num3.trim().parse().expect("Erro");
    
    println!("TOTAL = R$ {:.2}", num2 + (num3 * 0.15));
}