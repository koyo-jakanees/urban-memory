@main def hello: Unit = 
  println("Hello world!")
  println(msg)

def msg = "I was compiled by Scala 3. :)"

def double(ints: List[Int]): List[Int] = {
  val buffer = new ListBuffer[Int]()
  for (i <- ints) {
    buffer += i * 2
  }
  buffer.toList
}

val newNumbers = double(oldNumbers)
