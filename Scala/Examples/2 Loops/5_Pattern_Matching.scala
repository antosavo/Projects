def colorToNumber(color: String) = 
color match 
{
  case "Red" => 1
  case "Blue" => 2
  case "Green" => 3
  case "Yellow" => 4
  case _ => 0 //default case.
}

println("Red => " + colorToNumber("Red"))
println("Black => " + colorToNumber("Black"))



