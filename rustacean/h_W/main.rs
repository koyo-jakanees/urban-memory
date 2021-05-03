fn main() {
    let number = 5; // the first binding created using the name 'number'
    let number = number + 15; //different binding shadows the name 'number
    let number = number * 2; //a new binding is created
    println!("the number is : {}", number);
    println!("Hello, World!!");
}