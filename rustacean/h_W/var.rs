fn main() {
  let mut a_number = 10;
  let a_bool = true;

  println!("the number is {}", a_number);
  println!("the boolean is {}", a_bool);
  a_number = 15;
  println!("And now the number is {}", a_number);
}
// variable bindings are immutable by default
// mut keyword allows us to reassign the variable
