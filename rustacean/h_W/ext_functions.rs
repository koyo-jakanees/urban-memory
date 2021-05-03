fn main() {
    println!("Hello, world!");
    another_function();
    assert_eq!(is_divisible_by(2, 3), false);
    assert_eq!(is_divisible_by(5, 1), true);
    assert_eq!(is_divisible_by(24, 6), true); 
    // Arrays 
    let letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
    println!("first element of the array: {}", letters[0]);  // prints 'a'
    println!("second element of the array: {}", letters[5]); // prints 'b'
    // Vectors
    let three_numbers = vec![1, 2, 3];
    println!("Initial vector: {:?}", three_numbers);  // prints "[1, 2, 3]"
    
     // the vec! macro also accepts the same syntax as the array constructor
    let ten_zeroes = vec![0; 10];
    println!("Ten zeroes: {:?}", ten_zeroes); // prints [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

fn another_function() {
    println!("Hello from another function!");
}

fn is_divisible_by(dividend: u32, divisor: u32) -> bool {
    // If the divisor is zero, we want to return early with a `false` value
    if divisor == 0 {
      return false;
    }
    dividend % divisor == 0
}