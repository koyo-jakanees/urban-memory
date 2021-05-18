use std::collections::HashMap;

fn main() {
    let mut book_reviews: HashMap<String, String> = HashMap::new();
    
     // Review some books.
    book_reviews.insert(
        "Adventures of Huckleberry Finn".to_string(),
        "My favorite book.".to_string(),
    );
    book_reviews.insert(
        "Grimms' Fairy Tales".to_string(),
        "Masterpiece.".to_string(),
    );
    book_reviews.insert(
        "Pride and Prejudice".to_string(),
        "Very enjoyable.".to_string(),
    );
    book_reviews.insert(
        "The Adventures of Sherlock Holmes".to_string(),
        "Eye lyked it alot.".to_string(),
    );
    
    if !book_reviews.contains_key("Les Misérables") {
        println!("We've got {} reviews, but Les Misérables ain't one.",
        book_reviews.len());
    }

    let sherlock = "The Adventures of Sherlock Holmes";
    assert_eq!(book_reviews.contains_key(sherlock), true);
    println!("Book reviews contains Sherlock? {}", book_reviews.contains_key(sherlock));
    book_reviews.remove(sherlock);
    assert_eq!(book_reviews.contains_key(sherlock), false);

}