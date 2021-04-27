# Introduction to *Rust*

Rust as a safe alternativ to existing systems software languages like C and C++. Like the well known languags in the space rust doesn't have large runtime of garbage collector, which contrasts it with almost all other modern languages.

Unlike C & C++ Rust guarantees (close to 99%) memory safety . It prevents many of the bugs related to incorrect use of memory you might encounter in C or C++

A unique balance among perfomance, safety and implementation expressions. 

Patience Patience!! Rust requires bit of theoretical knowledge before you start writing productive Rust Code.

An open-source, systems programming language that helps write faster, more reliable software. It offers control over low-level details like memory usage in combination with high-level concepts like iterations and interfaces.

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

- create new project templates with the `cargo new` command
- Build a project with the `cargo build` command.
- Build and run a project with the `cargo run` commands
