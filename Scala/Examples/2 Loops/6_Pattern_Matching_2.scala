def f(x: Int, y: Int, operator: String): Double = 
{
  operator match 
  {
    case "+" => x + y
    case "-" => x - y
    case "*" => x * y
    case "/" => x / y.toDouble
  }
}

val sum = f(10,20, "+")
val product = f(10, 20, "*")


println("sum = " + sum)
println("product = " + product)



