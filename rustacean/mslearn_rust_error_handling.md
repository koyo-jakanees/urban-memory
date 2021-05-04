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
