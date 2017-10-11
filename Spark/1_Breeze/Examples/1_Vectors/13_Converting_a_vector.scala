import breeze.linalg._

val v = DenseVector.fill(5, 2)
val w = convert(v,Double)

println("v = " +v)
println("v(Double) = " +w)