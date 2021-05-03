fn main() {
    let number = 5; // the first binding created using the name 'number'
    let number = number + 15; //different binding shadows the name 'number
    let number = number * 2; //a new binding is created
    // let number_a: u32 = "42".parse().expect("Not a number");
    println!("the number is : {}", number);
    println!("Hello, World!!");
    let is_bigger = 1 > 4;
println!("{}", is_bigger); 
}