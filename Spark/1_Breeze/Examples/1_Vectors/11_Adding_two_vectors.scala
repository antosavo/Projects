import breeze.linalg._

val v = DenseVector.range(0, 5, 1)
val w = DenseVector.fill(5, 2)

println("v = " +v) //both Int
println("w = " +w) //both Int
println("v + w = " +(v + w)) //both Int

val a = DenseVector.rangeD(0, 5, 1)
val b = linspace(0, 1, 5)

println("a = " +a) //both Double
println("b = " +b) //both Double
println("a + b = " +(a + b)) //both Double

