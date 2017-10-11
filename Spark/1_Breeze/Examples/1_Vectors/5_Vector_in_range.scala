import breeze.linalg._

val v = DenseVector.range(0, 10)
println("v = " +v)

val w = DenseVector.range(0, 20, 2)
println("w = " +w)

val u = DenseVector.rangeD(0.5, 20, 2.5) //Double
println("u = " +u)
