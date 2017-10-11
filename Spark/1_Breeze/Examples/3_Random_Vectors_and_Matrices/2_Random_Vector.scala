import breeze.stats.distributions._
import breeze.linalg._
import breeze.numerics._ 

val v = DenseVector.rand(5) //uniformly distributed values between 0 and 1
println("v = " +v)

val u = DenseVector.rand(5, Uniform(0,10))
println("u = " +u)

val g = DenseVector.rand(5, Gaussian(5,1))
println("g = " +g)

val p = DenseVector.rand(5, Poisson(5))
println("p = " +p)