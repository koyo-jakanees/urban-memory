/* functional programming in rust
 * Lecture: https://www.youtube.com/watch?v=6dRy_K8IW5w
 * Rust is a multi-paradigm language.
 * Functional programming is the  process of building software by composing pure functions,
 * avoiding shared state, mutable data, and side-effects. Contrast with oop, where application
 * state is usually shared and colocated with methods in objects.
 * 
 * Pure functions: every input has one/same output. e.g f(x) = 2x. f(2) = 4
 * side effects: Any application state change that is observable outside the called function
 * other than its return value. e.g modifying global variable
 * FP tends to be more concise, predictable and easier to test than imperative or oop code 
 * but if unfamiliar with it and its common patterns, functional code can also seem alot more
 * dense and related literature impenetrabel for newbies
 * 
 * First Class Functions: functions are treated like any other variable. A function can be passed as an arg
 * other function and can be assigned to a variable.
 * 
 * Closure(first class function): anonymous fn u can save in a var or pass as arg to other fn
 * refer to the closure  using the name of the variable that is referring to it, but that does
 * not make it a named fn.
 * Closures can capture values from the scoper in which they're defined.
 * fn add_two(X:i32) -> i32 {x + 2} --> |x| x + 2
 * {
 * let x = 2;
 * let closure_ = || x;
 * }
 * 
 * Higher Order Functions: any fn which takes a fn as an arg, returns a fn, or both.
 * 
 * Example: Map(Morph Array Piece-by-Piece) fn --> takes a fn or closure and a list and applies that fn to every element
 * in the list producing a new list.
 * Takes a fn or closure and an iterable and applies that fn to every element in the iterable
 * producing a new iterable.
 * {
 * let v1: Vec<i32> = vec![1,2,3,4,5];
 * let v2: Vec<i32> = v1.iter().map(|x| x+1).collect();
 * }
 * 
 * Filter fn: constructs an iterator from elements of an iterable which a function returns true.
 * 
 * fn main(){
 *   let shoes = Vec![
 *     Shoe {size:10, style: String::from("sneaker")},
 *     Shoe {size:13, style: String::from("sandal")},
 *     Shoe {size:10, style: String::from("boot")},
 *    ];
 *   let in_my_size = shoes_my_size(shoes, 10);
 * }
 * Struct Shoe {
 *   size: u32,
 *   style: String,
 * }
 * 
 * fn shoe_my_size(shoes: Vec<Shoe>, shoe_size:u32) -> Vec<Shoe> {
 *   shoes.into_iter()
 *     .filter(|s| s.size == shoe_size)
 *     .collect()}
 * 
 * Fold fn: applies a function to an iterable, producing a single, final value.
 * Takes 2 args: an initial value, and a closure with 2 args(an accumulator, and an element.) The closure returns
 * the value that the accumulator should have for the next iteration.
 * 
 * let nums = [1,2,3];
 * 
 * let sum = nums.iter().fold(0, |acc, x| acc + x);
 * Chaining higher order functions together for powerful use cases.building an entire distributed data processing sytem
 * */
#[derive(PartialEq, Debug)]
