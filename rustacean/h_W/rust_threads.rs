// from cs196 illinois https://www.youtube.com/watch?v=JXDkdaGEuVU
use std::thread;
use std::time::Duration;
// use std::sync::mpsc;

fn main() {
    // let (tx, rx) = mpsc::channel();
    let handle = std::thread::spawn(move || {
        for i in 0..10 {
            println!("Hello number {} from the spawn thread", i);
            thread::sleep(Duration::from_millis(1));
        }
    });
    handle.join().unwrap();
    // position of the join function matters. if before the main thread it'll block main
    // until spawned is done
    for i in 1..5 {
        println!("hello simple number {} from main thread", i);
        thread::sleep(Duration::from_millis(1));
    }
    // handle.join().unwrap();
}