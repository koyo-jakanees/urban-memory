// Use the index notation to access the required elements of the numbers tuple and the letters array.
fn indexing_tuple() {
    let numbers = (1, 2, 3);
    // let second = todo!("Replace with the tuple indexing syntax");
    let second = numbers.1;

    assert_eq!(
        2, second,
        "This is not the 2nd number in the tuple: {}",
        second
    )
}

fn indexing_array() {
    let characters = ['a', 'b', 'c', 'd', 'e'];
    // let letter_d = todo!("Replace with the array indexing syntax");
    let letter_d = characters[3];

    assert_eq!(
        'd', letter_d,
        "This is not the character for the letter d: {}",
        letter_d
    )
}
fn main() {
    indexing_array();
    indexing_tuple();
}