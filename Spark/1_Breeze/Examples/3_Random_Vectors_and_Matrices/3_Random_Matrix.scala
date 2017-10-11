import breeze.stats.distributions._
import breeze.linalg._
import breeze.numerics._ 

val M = DenseMatrix.rand(3,3) //uniformly distributed values between 0 and 1
println("M :\n " +M)

val U = DenseMatrix.rand(3,3, Uniform(0,10))
println("U :\n " +U)

val G = DenseMatrix.rand(3,3, Gaussian(5,1))
println("G :\n " +G)

val P = DenseMatrix.rand(3,3, Poisson(5))
println("P :\n " +P)