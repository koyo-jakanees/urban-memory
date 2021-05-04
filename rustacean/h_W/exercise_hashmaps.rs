// In this exercise, you'll need to define a basket of fruit in the form of a hash map. 
// The key represents the name of the fruit. The value represents how many of that particular fruit are in the basket.

// You have to put at least three different types of fruit in the basket. 
// For example, three types might be apple, banana, and mango. The total count of all the fruits should be at least five.

// You only need to edit the fruit_basket function in this exercise
use std::collections::HashMap;

fn fruit_basket() -> HashMap<String, u32> {
    let mut basket: HashMap<String, u32> = HashMap::new();

    // Two bananas are already given for you :)
    basket.insert(String::from("banana"), 2);
    basket.insert(String::from("Apple"), 5);
    basket.insert(String::from("Lemon"), 10);
    basket.insert(String::from("Pineapple"), 4);
    basket.insert(String::from("grapes"), 6);
    basket.insert(String::from("Mangoes"), 6);

    // TODO: Put more fruits in your basket here.

    basket
}

fn main() {
    let basket = fruit_basket();
    let kinds = basket.len();
    let pieces = basket.values().sum::<u32>();
    assert!(
        basket.len() >= 3,
        "basket must have at least three types of fruits"
    );
    println!("We have {} types of fruits", basket.len());
    assert!(
        basket.values().sum::<u32>() >= 5,
        "basket must have at least five fruits"
    );

    // Show our fruit basket
    println!("The basket has {} pieces of {} different kinds of fruit.", pieces, kinds);
}