# Error Handling

Error handling is the process of anticipating and working with the possibility of failure.

For example, a program's failure to read a file, followed by its continuing use of that bad input, would clearly produce problematic errors. Your ability to notice and explicitly manage those errors can save the program from various additional pitfalls.

- Use `panic!` to deal with unrecoverable errors.
- Use the `Option` enum when a value is optional or the lack of a value is not an error condition.
- Use the `Result` enum when things could go wrong and a caller might have to deal with the problem.

Panicking is the simplest error handling mechanism in Rust.

```rust
fn main() {
    panic!("Farewell!");
}
```

```sh
# terminal panick output
thread 'main' panicked at 'Fare Thee well!!', panick.rs:2:5
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
The preceding panic message reveals the place in the source code where the panic occurred, `src/main.rs:2:5`. The message indicates that it’s the fifth character on the second line of the `src/main.rs` file.
In general terms, you should use `panic!` when a program reaches an unrecoverable state meaning anything where there is absolutely no way to recover from the error.
Rust panics on some operations such as a _division by zero_ or an attempt to access an index that isn't present in an array, a vector, or a hash map, as shown in the following code

```rust
let v = vec![0, 1, 2, 3];
println!("{}", v[6]); // this will cause a panic!
```

#### The `Option` type

The Rust standard library offers `Option<T>` enum to be used when the absences of a value is a possibility.
Commonly used coz it encodes the very common scenario in which a value could be something or it could be nothing
Rust is explicit about when a value is optional. While in many languages, a function that takes a `String` might actually take either a `String` or `null,` in Rust, that same function can only take actual `Strings`.
If you want to model an optional string in Rust, you need to explicitly wrap it in an Option type: `Option<String>.`

```rust
enum Option<T> {
    None,     // The value doesn't exist
    Some(T),  // The value exists
}
```
The `<T>` part of the `Option<T>` enum declaration states that the type `T` is generic and will be associated with the `Some` variant of the `Option` enum.

trying to access a vector's non-existent index would cause the program to `panic`, but you could avoid that by using the `Vec::get` method, which returns an `Option` type instead of panicking. If the value exists at a specified index, it's wrapped in the `Option::Some(value)` variant. If the index is out of bounds, it would return a `Option::None` value instead.
[Rust playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=14dcb7b524b0448c946b85ef9b28908c%3Fazure-portal%3Dtrue)

```rust
let fruits = vec!["banana", "apple", "coconut", "orange", "strawberry"];

// pick the first item:
let first = fruits.get(0);
println!("{:?}", first);

// pick the third item:
let third = fruits.get(2);
println!("{:?}", third);

// pick the 99th item, which is non-existent:
let non_existent = fruits.get(99);
println!("{:?}", non_existent);
```
Output of the above:
```sh

Some("banana")
Some("coconut")
None
```
Explanation:
>The printed message says that the first two attempts at accessing the existing indexes in the fruits array resulted in `Some("banana")` and `Some("coconut"),` but the attempt to fetch the 99th element returned a `None` value (which isn't associated with any data) instead of panicking.
> In practice, you must decide how your program behaves depending on what enum variant it gets. But how can we access the data inside a `Some(data)` variant?

### Pattern Matching
An extremely powerful control flow operator called `match`, which you can use to compare a value against a series of patterns and then execute code based on which pattern matches.
Example:[Rust playground](https://play.rust-lang.org/?version=nightly&mode=debug&edition=2018&gist=060f6d3ffa5186f8287f56d1e24cca1e%3Fazure-portal%3Dtrue)
```rust
let fruits = vec!["banana", "apple", "coconut", "orange", "strawberry"];
for &index in [0, 1, 2, 3, 4, 5, 6, 7, 99].iter() {
    match fruits.get(index) {
        Some(fruit_name) => println!("It's a delicious {}!", fruit_name),
        None => println!("There is no fruit! :("),
    }
}
```
Output
```sh
It's a delicious banana!
It's a delicious apple!
It's a delicious coconut!
It's a delicious orange!
It's a delicious strawberry!
There is no fruit! :(
There is no fruit! :(
There is no fruit! :(
There is no fruit! :(
```
Explanation:
> we iterate through the same indexes from our previous example (0, 2, and 99) and then use each one to retrieve a value from the `fruits` vector by using the _fruits.get(index)_ expression.
> Because the `fruits` vector contains `&str` elements, we know that the result of this expression is of type `Option<&str>`. You then use a match expression against the `Option` value and define a course of action for each of its variants. Rust refers to those branches as match arms, and each arm can handle one possible outcome for the matched value.
```rust
fn main() {
    let fruits = vec!["banana", "apple", "coconut", "orange", "strawberry"];
    for &index in [0, 1, 2, 3, 4, 5, 6, 7, 99].iter() {
        match fruits.get(index) {
            Some(&"coconut") => println!("Coconuts are awesome!!!"),
            Some(fruit_name) => println!("It's a delicious {}!", fruit_name),
            None => println!("There is no fruit! :("),
        }
    }
}
```
Output: 
```sh
It's a delicious banana!
It's a delicious apple!
Coconuts are awesome!!!
It's a delicious orange!
It's a delicious strawberry!
There is no fruit! :(
There is no fruit! :(
There is no fruit! :(
There is no fruit! :(
```
Explanation:
>The first pattern in the match is `Some(&"cocounut")` (note the `&` before the string literal). This is because `fruits.get(index)` returns an `Option<&&str>` or an option of a reference to a string slice. Removing `&` in the pattern would mean we are trying to match against an `Option<&str>` (an optional string slice not an optional reference to a string slice). We haven't covered references so this might not make full sense right now. For now, just remember the `&` is making sure the types line up properly.
> Note that when the string value is "coconut", the first arm is matched and then used to determine the flow of execution.

Rules to keep in mind when using _match_ expression
- `match` arms are evaluated from top to bottom. Specific cases must be defined earlier than generic cases or they'll never be matched and evaluated.
- `match` arms must cover every possible value that the input type could have. You'll get a compiler error if you try to match against a non-exhaustive pattern list.

#### _if let_ expression

test whether a value conforms with a single pattern.
example, which matches on an `Option<u8>` value but wants to execute code only if the value is 7
```rust
let some_number: Option<u8> = Some(7);
match some_number {
    Some(7) => println!("That's my lucky number!"),
    _ => {},
}
```
We want to do something with the `Some(7)` match but ignore other `Some<u8>` values or the `None` variant. You can add the `_` (underscore) wildcard pattern after all other patterns to match anything else, and it's used to satisfy the compiler demands for exhausting match arm

a shorter way by using an _if let_ expression

```rust
if let Some(7) = some_number {
    println!("That's my lucky number!");
}
```
code explanation:
>An _if let_ expression takes a pattern and an expression separated by an equal sign. If the pattern matches, the _if_ block is executed. The nice thing about _if let_ expressions is that you don't need all the boilerplate code of a match expression when you're interested in a single pattern to match against.

#### `Unwrap` and `expect`

You can try to access the inner value of an `Option` type directly by using the` unwrap` method. Be careful, though, because this method will panic if the variant is a `None`.

```rust
let gift = Some("candy");
assert_eq!(gift.unwrap(), "candy");

let empty_gift: Option<&str> = None;
assert_eq!(empty_gift.unwrap(), "candy"); // This will panic!
```
Compiler panic
```sh
   Compiling playground v0.0.1 (/playground)
    Finished dev [unoptimized + debuginfo] target(s) in 1.46s
     Running `target/debug/playground`
thread 'main' panicked at 'called `Option::unwrap()` on a `None` value', src/main.rs:14:27
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
The `expect` method does the same as `unwrap`, but it provides a custom panic message that's provided by its second argument

```rust
let a = Some("value");
assert_eq!(a.expect("fruits are healthy"), "value");

let b: Option<&str> = None;
b.expect("fruits are healthy"); // panics with `fruits are healthy`
```
Because this functions might panic it is recommended to not use them.
- Use pattern matching and handle the `none` case explicitly
- Call similar non-panicking methods, such as `unwrap_or`, which returns a default value if the variant is `none` or the inner value if the variant is `Some(value)`

```rust
assert_eq!(Some("dog").unwrap_or("cat"), "dog");
assert_eq!(None.unwrap_or("cat"), "cat");
```
##### Exercise
[rust playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=bfc7568619b261d18e272bf09bad48c0%3Fazure-portal%3Dtrue)
In this exercise, you'll finish implementing a function that receives a Person struct and returns a String that contains its full name.
```rust
struct Person {
    first: String,
    middle: Option<String>,
    last: String,
}

fn build_full_name(person: &Person) -> String {
    let mut full_name = String::new();
    full_name.push_str(&person.first);
    full_name.push_str(" ");

    // TODO: Implement the part of this function that handles the person's middle name.

    full_name.push_str(&person.last);
    full_name
}

fn main() {
    let john = Person {
        first: String::from("James"),
        middle: Some(String::from("Oliver")),
        last: String::from("Smith"),
    };
    assert_eq!(build_full_name(&john), "James Oliver Smith");

    let alice = Person {
        first: String::from("Alice"),
        middle: None,
        last: String::from("Stevens"),
    };
    assert_eq!(build_full_name(&alice), "Alice Stevens");

    let bob = Person {
        first: String::from("Robert"),
        middle: Some(String::from("Murdock")),
        last: String::from("Jones"),
    };
    assert_eq!(build_full_name(&bob), "Robert Murdock Jones");
}
```