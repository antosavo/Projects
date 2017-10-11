import breeze.linalg._

val v = DenseVector.fill(5, 2)
val w = DenseVector.range(0, 5, 1)

println("v = " +v)
println("w = " +w)

val u = DenseVector.vertcat(v,w)

println("vertical concat(v,w) = " +u)

val M = DenseVector.horzcat(v,w)

println("horizontal concat(v,w) = \n" +M)