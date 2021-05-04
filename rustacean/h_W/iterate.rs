fn main() {
    let formal = true;
    let greeting = if formal {
        "Good evening."
    } else {
        "Hello, friend!"
    };
    println!("{}",greeting); // prints "Good evening."
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}