import breeze.linalg._

val v = linspace(0, 9, 10)
println("v = " +v)

val w = v.slice(4, 7)
println("w = " +w)

val u = v.slice(0, v.size, 2) //even position
println("u = " +u)