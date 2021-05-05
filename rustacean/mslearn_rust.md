# Introduction to Rust

Notes from [Microsoft Learn](https://docs.microsoft.com/en-us/learn/modules/rust-understand-common-concepts/7-collection-types):

Rust as a safe alternativ to existing systems software languages like C and C++. Like the well known languags in the space rust doesn't have large runtime of garbage collector, which contrasts it with almost all other modern languages.

Unlike C & C++ Rust guarantees (close to 99%) memory safety . It prevents many of the bugs related to incorrect use of memory you might encounter in C or C++

A unique balance among perfomance, safety and implementation expressions. 

Patience Patience!! Rust requires bit of theoretical knowledge before you start writing productive Rust Code.

An open-source, systems programming language that helps write faster, more reliable software. It offers control over low-level details like memory usage in combination with high-level concepts like iterations and interfaces.

It useful for both low-level and high-level types of develoment
`rustup` tool used to set up a development environment in rust
`rustc` used to write and compile rust programs
`cargo` start new project template, build and run rust programs

Rust Pros offers.

- **Type Safe**:
    The compiler assures that no operation will be applied to a variable of a wrong type

- **Memeory Safe**:
    Rust pointer(_references_) always refer to valid memory

- **Data race-free**:
    The borrow checker guarantees thread-safety by ensuring that multiple parts of a program can't mutate the same value at the same time

- **Zero cost abstraction**:
    Allows the use of high-level concepts, like iteration, interfaces, and functional programming, with minimal to no perfomance costs. The abstraction perform as well, as if you wrote the underlying code by hand.

- **Minimal runtime**:
    Very minimal and optimal runtime. It has no garbage collector to manage memory efficiently. Most similar to C & C++.

To install rust visit [here](https://rustup.rs/), or directly run this in  your terminal 

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Use `rustc` compiler for simple programs. For bigger projects, the build tool and dependency manager `cargo` suits better.

some of the **cargo** functionalities:

- create new project templates with the `cargo new` cmd.
- Build a project with the `cargo build` cmd.
- Build and run a project with the `cargo run` cmd.
- Test a project with `cargo test` cmd.
- Check project types with `cargo check` cmd.
- Build documentation for a project with `cargo doc` cmd.
- Publish a library to crates.io with `cargo publish` cmd.

## Create new project.

Change to your working directory and use the cmd.

```sh
cargo new NameOfProject
```

This cmd generates a new dir with the given name with a src directory and two files:

```sh
cd hello-cargo
tree .
├── Cargo.toml
└── src
    └── main.rs

1 directory, 2 files
```

- *__Cargo.toml__* file: 
        the manifest file for rust, Metadata and any dependencies for the project is stored here

```rust
fn main() {
     println!("Hello, world!");
}
```

- *__main.rs__* file:
     in the src subdirectory, entry point for your application code
     > `cargo new` generates a boilerplate `"Hello world!"` project

```toml
[package]
name = "hello-cargo"
version = "0.1.0"
authors = ["Your Name <you@example.com>"]
edition = "2018"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

## Build the project

Before delving into code, try and run the boilerplate code by doing the following:

```sh
cd hello-cargo
cargo run
```
sample output of the commands above,
```sh
   Compiling hello-cargo v0.1.0 (/home/ichigo/old/home/geopro/Documents/pyqt/fileIO/urban-memory/rustacean/hello-cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.86s
     Running `target/debug/hello-cargo`
Hello, world!
```
for indepth coverage
[cargo book](https://doc.rust-lang.org/cargo/guide/why-cargo-exists.html)
>Cargo is the Rust package manager. It is a tool that allows Rust packages to declare their various dependencies and ensure that you’ll always get a repeatable build.

>To accomplish this goal, Cargo does four things:

> - Introduces two metadata files with various bits of package information.
>  - Fetches and builds your package’s dependencies.
>  - Invokes rustc or another build tool with the correct parameters to build your package.
>  - Introduces conventions to make working with Rust packages easier.

The `cargo run` cmd combines two process i.e `cargo build` to generate/compile the binary [binary crate](https://doc.rust-lang.org/cargo/appendix/glossary.html#crate) and the `run` the crate/program in  one step

```sh
#step 1
cargo build
   Compiling hello_world v0.1.0 (file:///path/to/package/hello_world)
# step 2
./target/debug/hello_world
Hello, world!
```

`cargo.lock` file contains information about programm dependencies
`cargo build --release` to compile files with optimizations turned on oce ready fo a release.

`... --release` puts the resulting binary in `target/release` instead of `target/debug`
compiling in debug mode by default for development which is shorte since compiler doesn't do optimizations, but the code execution will be slower. Release mode is the opposite.

Rust comes with built-in data types to express numbers, text and truthiness.

### Numbers

Integers can be identified by bit size and the signed property. Signed Integers can represent positive and negative numbers.
Unsigned represent only positive numbers.

| Length	|Signed |	Unsigned|
| :-------: |:-------: | :-------:|
|8-bit	 | i8	|  u8     |
|16-bit	 | i16	|  u16  |
|32-bit	 | i32	|  u32  |
|64-bit	 | i64	|  u64  |
|128-bit | i128	|  u128  |
|arch	 | isize|  usize  |

`isize` and `usize` types depend on the kind of computer your program is running on: 64-bit if you're on 64-bit architecture and 32 bit if you're 32-bit architecture.
The default type assigned to integers whenever you don't specify one/

Rust's floating point type are `f32` and `f64` which are 32 and 64 bits respectively.
the default type is `f64` because on modern CPU's it's roughly same speed as `f32` but is  capable of more precision.

```rust
let x = 2.0; //f64, the default type
let y: f32 = 3.0; //f32, via type annotation
```

primitive number types support mathematical operations such as [`addition, subtraction, multiplication and division`](https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=d683842bd8cedd949ed3c56b27f6f0eb%3Fazure-portal%3Dtrue)

```rust
fn main() {
    // Addition
    println!("1 + 2 = {}", 1u32 + 2);

    // Subtraction
    println!("1 - 2 = {}", 1i32 - 2);
    // ^ Try changing `1i32` to `1u32` to see why the type is important

    // Integer Division
    println!("9 / 2 = {}", 9u32 / 2);

    // Float Division
    println!("9 / 2 = {}", 9.0 / 2.0);

    // Multiplication
    println!("3 * 6 = {}", 3 * 6)
}
```

### Booleans

Booleans in Rust are represented by the type `bool` and have two possible values: `true or false`. They're used widely in conditionals, such as `if` and `else` expressions

```rust
let is_bigger = 1 > 4;
println!("{}", is_bigger);  // prints "false"
```

### Character and Strings

Rust has two string types and one character type. All of them are valid UTF-8 representations.
The `char` type is the most primitive type among them and is specified with single quotation marks:

```rust
let c = 'z';
let z = 'ℤ';
let heart_eyed_cat = '😻';
```

The `str` type, also known as a `string slice`, is a view into string data. Most of the time, we refer to those types in referenced form by using the form `&str`. We'll cover references in the following modules. For now, you can think of `&str` as a pointer to an immutable string data. String literals are all of type `&str`.

Although string literals are convenient to use in introductory Rust examples, they aren't suitable for every situation in which we might want to use text. That's because not every string can be known at compile time. An example is when a user interacts with a program and sends text via a terminal.

For these situations, Rust has a second string type, `String.` This type is allocated on the heap. It can store an amount of text that's unknown to us at compile time.

```rust
let mut hello = String::from("Hello, ");  // create a String from a string literal
hello.push('w');                          // push a character into our String
hello.push_str("orld!");                  // push a string literal into our String
println!("{}", hello)
```

### Tuples

A tuple is a grouping of values of different types collected into one compound. They have fixed length, meaning that after they're declared, they can't grow or shrink in size. The type of a tuple is defined by the sequence of each member's type.

```rust
("hello", 5i32, 'c');
```

This tuple has the type signature (`&'static str, i32, char`), where:

- `&'static` str is the type of the first element.
- `i32` is the type of the second element.
- `char` is the type of the third element.

Tuples elements can be accessed by position, which is known as tuple indexing. It looks like this:

```rust
fn main() {
  let tuple = ("hello", 5, 'c');

  assert_eq!(tuple.0, "hello");
  assert_eq!(tuple.1, 5);
  assert_eq!(tuple.2, 'c');
}
```

`assert_eq!` macro verifies that two expressions are equal to each other.
Tuples are useful when you want to combine different types into a single value. For instance, functions can use tuples to return multiple values because tuples can hold any number of values

### Structs and Enums

Struct is a type that's composed of other types, like tuples. The pieces of a struct can be different types, but you can name each piece of data so it's clear what values mean.

structs in rust comes in 3 flavors. `classic, tuple and unit structs`

```rust
// A struct with named fields
struct Person {
    name: String,
    age: u8,
    likes_oranges: bool
}

// A tuple struct
struct Point2D(u32, u32);

// A unit struct
struct Unit;
```

- __classic struct__:  [C Structs](https://en.wikipedia.org/wiki/Struct_(C_programming_language)) most commonly used. Each field defined within them has a name and a type. After they're defined, they can be accessed by using `example_struct.field` syntax
- __Tuple Struct__: similar to classic struct, but their fields have no names. For accessing individual variables, the same syntax is used as with regular tuples, namely `foo.0`, `foo.1` and so on. Starting at zero.
- __Unit Struct__: Are most commonly used as markers.
  
#### Instantiate Structs

```rust
// A struct with named fields
struct Person {
    name: String,
    age: u8,
    likes_oranges: bool
}

// A tuple struct
struct Point2D(u32, u32);

// A unit struct
struct Unit;

fn main() {
    // Instantiate a regular struct, with named fields. Order does not matter.
    let person = Person {
        name: String::from("Adam"),
        age: 25,
        likes_oranges: true
    };
    
    // Instantiate a tuple struct by passing the values in the same order as defined.
    let origin = Point2D(0, 0)
    
    // Instantiate a unit struct.
    let unit = Unit;
}
```

### Enums

Are types that can be any of several variants.

What Rust calls enums are more commonly known as [algebraic data types](https://en.wikipedia.org/wiki/Algebraic_data_type) if you're coming from a functional programming background. The important detail is that each enum variant can have data to go along with it.

`Enum` keyword allows the creation of a type which might be one of  few different variants. Enum variants just like structs, can have fields  with names,fields without names or no fields at alll.

Define an enum to classify a web event. Each variant is independent and stores different amounts and types of values.

```rust
enum WebEvent {
    // An enum may either be unit-like,
    PageLoad,
    PageUnload,
    // An enum can include characters and strings
    KeyPress(char),
    Paste(String),
    // or include tuple structs
    Click { x: i64, y: i64 },
}
```

- `PageLoad` and `PageUnload` have no data associated with it at all.
- `Keypress` includes a single character in it.
- `Paste` includes a single string.
- `Click` includes an anonymous struct inside it.

Defining an enum with variants such as the preceding one is similar to defining different kinds of struct definitions. All the variants are grouped together under the same WebEvent type and each variant is not its own type. This means we can't have functions that only accept KeyPress and not other variants of the WebEvent enum.

We can chose to define separate structs for each variant and then have each variant hold on to the different structs. These would hold the same data that the preceding enum variants held. But this definition would allow users to refer to each logical variant on its own.

```rust
enum WebEvent {
    PageLoad,
    PageUnload,
    KeyPress(KeyPress),
    Paste(String),
    Click(Click)
}

struct Click { 
    x: i64, 
    y: i64 
}

struct KeyPress(char);
```

Now in your code you can refer to a `WebEvent::Click` which is a variant of the type `WebEvent` and you can also just refer to `Clicks` on their own separate from `WebEvent`s.

#### Exercise - Fix the code with structs and enums

Let's build cars!

Edit only the `car_factory `function so that it can return `Car` objects as requested by the clients.

#### Creating reusable functionality with functions.

Functions are the primary way code is executed in rust. The `main` function is the entry point of many programs.
Function definitations in rust start with `fn` and have a set of parenthesis after the function name.

```rust
fn main() {
    println!("Hello, world!");
    another_function();
}

fn another_function() {
    println!("Hello from another function!");
}
```

#### passing parameters to functions

```rust
fn is_divisible_by(dividend: u32, divisor: u32) -> bool {
  // If the divisor is zero, we want to return early with a `false` value
  if divisor == 0 {
    return false;
  }
  dividend % divisor == 0
}
```

- `fn`: The function declaration keyword in Rust.
- `is_divisible_by`: The function name.
- `(dividend: u32, divisor: u32)`: This function's parameter list. It states that two unsigned 32-bit integers are expected as input values.
- `-> bool`: The arrow points to the type of value this function will always return.
The `is_divisible_by `function accepts two integers as inputs and outputs a boolean value

### Collection types.

Rust has many other compound types that can group multiple values into a single type.

#### Arrays:

A collection of objects of the same type, which is stored sequentialy in memory. Created by using `[]`. Their size which is known at compile time is part of their signature `[T; size]` where `T` is the type of the values in the array and `size` in a non-negative integer checked at compile time.
> Arrays have fixec length and every element of an array must be of the same type.

- comma-separated list inside brackets
- The initial value, followed by a semicolon, and then the length of the array in brackets

```rust
fn main() {
  // a comma-separated list inside of brackets
  let weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

  // initialize an array of 512 elements where every element is a zero
  let byte_buffer = [0_u8; 512];
}
```

Arrays are useful when you want your data allocated on the stack rather than the heap. They're also useful when you want to ensure you always have a fixed number of elements.
You can access elements of an array by using indexing, which starts at 0

```rust
let letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
println!("first element of the array: {}", letters[0]);  // prints 'a'
println!("second element of the array: {}", letters[1]); // prints 'b'

```

Since the array length is known at compile time, Rust makes it impossible to build any program that attempts to access an array out of its bounds with an index known at compile time.
#### Vectors

you can use vectors with the type `Vec<T>` to store multiple values of the same type. Unlike arrays, vectors can grow or shrink at any time. This capability is implied in their size not being known at compile time, so Rust can't prevent you from accessing an invalid position in your vector.
> You'll notice the syntax `<T>` often in Rust. These are generic type parameters. When we write `Vec<T>,` what we're indicating is a `Vec` type composed of some type `T`. The name `T` is conventionally used as a type name for a type we don't yet know. When we actually create vectors, they'll have concrete types like `Vec<u32>` or `Vec<String>`.

You can use the `vec!` macro to initialize a vector.

You might have noticed the `{:?}` format parameter inside the `println!` calls. It's used whenever we want to print something for debugging reasons, whereas `{}` is used for displaying information to an end user. Because Rust doesn't know how to represent a vector of integers to end users, using the former mark would result in a compilation error. We're going to learn precisely how to do that when we reach the `"Traits"` module in this course.

Vectors can also be created by using the `Vec::new()` method. You can push values onto the end of a vector, which will grow the vector as needed:

```rust
let mut v = Vec::new();  // creates an empty vector,
v.push(5);               // pushes the number five into it...
v.push(6);               // ... an then six, and so on
v.push(7);
v.push(8);
println!("{:?}", v); // prints [5, 6, 7, 8]
```

Popping values works in much the same way:

```rust
let mut v = vec![1, 2];
let two = v.pop();
```

Vectors also support indexing:

```rust
let mut v = vec![1, 2, 3];
let three = v[2];
v[1] = v[1] + 5;
```

If you try to use an index value that the vector doesn't have an element for, the program will enter an unrecoverable panic state and terminate its thread.

As an example, let's see what a program will do if it has a vector that holds five elements and then tries to access an element at index 100:

```rust
let v = vec![1, 2, 3, 4, 5];
let does_not_exist = v[100];
```

```sh
# output
   Compiling playground v0.0.1 (/playground)
    Finished dev [unoptimized + debuginfo] target(s) in 4.04s
     Running `target/debug/playground`
thread 'main' panicked at 'index out of bounds: the len is 5 but the index is 100', src/main.rs:3:26
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

### Hash Maps

The type `HashMap<K, V>` stores a mapping of keys of some type `K` to values of some type `V`. Where vectors store values by an integer index, hash maps store values by key.
Many programming languages support this kind of data structure. They often use a different name, such as hash, map, object, hash table, dictionary, or associative array, to name a few.

Like vectors, hash maps are growable, store the data in the heap, and access to its items are checked at run time.

In the following example, we're keeping track of a personal book review system. The keys are the book names, and the values are the reviews made by one specific user.

You can create an empty hash map by using the `HashMap::new` method and then adding elements with the `HashMap::insert` method.

```rust
use std::collections::HashMap;

let mut book_reviews: HashMap<String, String> = HashMap::new();

// Review some books.
book_reviews.insert(
    "Adventures of Huckleberry Finn".to_string(),
    "My favorite book.".to_string(),
);
book_reviews.insert(
    "Grimms' Fairy Tales".to_string(),
    "Masterpiece.".to_string(),
);
book_reviews.insert(
    "Pride and Prejudice".to_string(),
    "Very enjoyable.".to_string(),
);
book_reviews.insert(
    "The Adventures of Sherlock Holmes".to_string(),
    "Eye lyked it alot.".to_string(),
);
// querying the populated hash map
if !book_reviews.contains_key("Les Misérables") {
    println!("We've got {} reviews, but Les Misérables ain't one.",
    book_reviews.len());
}
```
You can see from the first line that we need to use `HashMap` from the `collections` portion of the standard library to bring its name into scope. This use is similar to what other programming languages call an `import`.

The next notable aspect of the preceding snippet is the use of the `.to_string()` method invocation. This method transforms a string literal `(&str)` value into `String`. This method is useful when we want our hash map to "own" the values it holds, instead of being a collection of references _(pointers)_. We'll cover those differences in detail when we reach the "Ownership and Borrowing" module.

Hash maps can use references to query for existing entries, which means that even if our hash map is of type `HashMap<String, String>`, we can use the `&str` or `&String` types to look up its keys

Just like with vectors, looking for a nonexistent key causes the program to panic:

```rust
// Searching for an existing key returns the value associated to it
println!("Review for Jane: {}", book_reviews["Pride and Prejudice"]);

// But searching for a nonexisting key will cause a panic
println!("Review for Herman: {}", book_reviews["Moby Dick"]);  // panics!
```

Hash maps also have the `.get()` method for safely querying their content without causing any panic
We can remove entries from a hash map by using the `.remove()` method
```rust
let sherlock = "The Adventures of Sherlock Holmes";
assert_eq!(book_reviews.contains_key(sherlock), true);
book_reviews.remove(sherlock);
assert_eq!(book_reviews.contains_key(sherlock), false);
```

### Control Flow

#### `if/else` expressions

The form of an `if` expression is a condition expression followed by a consequent block, any number of `else if` conditions and blocks, and an optional trailing `else` block. The condition expressions must have type `bool`.
```rust
if 1 == 2 {
    println!("whoops, mathematics broke");
} else {
    println!("everything's fine!");
}
```
In the preceding example, the condition of `if` is the expression `1 == 2`, which evaluates into a boolean type with the value _false_.
Unlike in most languages, if blocks can also act as expressions. Remember that all branches must return the same type for our code to compile.
```rust
let formal = true;
let greeting = if formal {
    "Good evening."
} else {
    "Hello, friend!"
};
println!(greeting) // prints "Good evening."
```
You can have multiple conditions by combining `if` and `else` in an `else if` expression
```rust
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
```
If a condition expression evaluates to `true`, the consequent block is executed. Any subsequent `else if` or `else` block is skipped. If a condition expression evaluates to `false`, the consequent block is skipped. Any subsequent `else if` condition is evaluated. If all `if` and `else if` conditions evaluate to `false`, then any `else` block is executed

#### Loop forever with `loop`

A `loop` expression denotes an `infinite loop`. It repeats execution of its body continuously:
If you decide to try running  the compiled version, just  hit `ctrl + C` to keyboard interrupt.

```rust
loop {
    println!("I loop forever");
}
```
Unlike the other kinds of loops in Rust like while and for, `loop` can be used in expressions that return values via `break`.

#### Loop until a criteria is met with `while` loops

A `while` expression loops until a predicate is _false_.

A `while` loop begins by evaluating the boolean loop conditional expression. If the loop conditional expression evaluates to `true`, the loop body block executes. Control then returns to the loop conditional expression. If the loop conditional expression evaluates to `false`, the _while_ expression completes.

```rust
let mut counter = 0;

while counter < 10 {
    println!("hello World!!");
    counter = counter + 1;
}
```

#### Iterate with `for` loops

A `for` expression extracts values from an iterator. It loops until the iterator is empty.

In Rust, an iterator is any type that can iterate over values. Some values can be iterated over directly and others can produce iterators by calling methods like `.iter()`

```rust
let a = [10, 20, 30, 40, 50];

for element in a.iter() {
    println!("the value is: {}", element);
}
```
The preceding code iterates through each element in the array and binds it to the `element` variable. The `println!` macro then prints each of those values in sequence.
Another easy way to create an iterator is to use the range notation `a..b`. This notation yields values from `a` (inclusive) to `b` (exclusive) in steps of one.

```rust
for item in 0..5 {
    println!("{}", item * 2);
}
```
The preceding code iterates through the numbers 0, 1, 2, 3, and 4 and binds it to the `item` variable for each cycle of this loop.
