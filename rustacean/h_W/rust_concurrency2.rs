use std::sync::Mutex;
// use std::thread;

fn main() {
    let m = Mutex::new(10);

    {
        let mut num = m.lock().unwrap();
        *num = 6;
    }
    println!("m =  {:?}", m);
}