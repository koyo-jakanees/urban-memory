use std::thread;
use std::sync::mpsc;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();
    let tx1 = mpsc::Sender::clone(&tx);

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("rust"),
            String::from("Thread"),
            ];
        for val in vals {
            tx1.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
        // println!("val is {}", val)
    });
    thread::spawn(move || {
        let vals = vec![
            String::from("More"),
            String::from("from"),
            String::from("the"),
            String::from("rust"),
            String::from("Threads"),
            ];
        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
        // println!("val is {}", val)
    });

    // let received = rx.recv().unwrap();
    for received in rx{
        println!("Got : {}", received)
    }
}