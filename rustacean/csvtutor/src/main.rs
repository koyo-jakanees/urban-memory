// official rust csv crate tutorial
// https://docs.rs/csv/1.1.6/csv/tutorial/index.html
// the cookbook: https://docs.rs/csv/1.1.6/csv/cookbook/index.html

// import standard library's I/O module to read from stdin
use std::error::Error;
use std::io;
use std::process;

// the 'main' function where the program starts
fn main() {
    println!("Hello, world!");
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }

}

fn run() -> Result<(), Box<dyn Error>> {
    let mut reader = csv::Reader::from_reader(io::stdin());

    // loop over each record in the file
    for result in reader.records() {
        // examine the result
        // if there's no problem, print the record otherwise print the error messeg
        let record = result?;
        // print a debug version of the record
        println!("{:?}", record)
        // match result {
        //     Ok(record) => println!("{:?}", record),
        //     Err(err) => {
        //         println!("error reading CSV from <stdin>: {}", err);
        //         process::exit(1);
        //     }
        // }
    }
    Ok(())
}