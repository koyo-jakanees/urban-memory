// official rust csv crate tutorial
// https://docs.rs/csv/1.1.6/csv/tutorial/index.html
// the cookbook: https://docs.rs/csv/1.1.6/csv/cookbook/index.html

// import standard library's I/O module to read from stdin
use std::env;
use std::ffi::OsString;
use std::error::Error;
// use std::io;
use std::fs::File;
use std::process;

// the 'main' function where the program starts
fn main() {

    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }

}
fn get_first_arg() -> Result<OsString, Box<dyn Error>>{
    match env::args_os().nth(1){
        None => Err(From::from("Expected 1 argument, but got none")),
        Some(file_path) => Ok(file_path),
    }
}

fn run() -> Result<(), Box<dyn Error>> {
    let file_path = get_first_arg()?;
    let file = File::open(file_path)?;
    // let mut reader = csv::Reader::from_reader(file);
    let mut reader = csv::ReaderBuilder::new()
        .has_headers(true)
        .from_reader(file);
    // or conviniently use  csv::Reader::from_path to automatically open file path.
    // {
    //     // nest headers in their own scope coz of rust lifetimes
    //     let headers = reader.headers()?;
    //     println!("{:?}", headers);
    // }

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
    // We can ask for the headers at any time. There's no need to nest this
    // call in its own scope because we never try to borrow the reader again.
    let headers = reader.headers()?.clone();
    println!("Headers: {:?}", headers);
    Ok(())
}