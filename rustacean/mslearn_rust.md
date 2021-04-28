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
authors = ["git local name <yourmail.com>"]
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