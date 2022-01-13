use std::io::{stdin};

fn main() {
    let mut num1 = String::new();    
    let mut num2 = String::new();
    let mut num3 = String::new();
    stdin().read_line(&mut num1).expect("Erro");
    stdin().read_line(&mut num2).expect("Erro");
    stdin().read_line(&mut num3).expect("Erro");
    
    let num1: f32 = match num1.trim().parse() {
        Ok(num) => num,
        Err(_) => 0.0
    };
    let num2: f32 = match num2.trim().parse() {
        Ok(num) => num,
        Err(_) => 0.0
    };
    let num3: f32 = match num3.trim().parse() {
        Ok(num) => num,
        Err(_) => 0.0
    };
    
    println!("MEDIA = {:.1}", (num1 * 2. + num2 * 3. + num3 * 5.) / 10.);
}