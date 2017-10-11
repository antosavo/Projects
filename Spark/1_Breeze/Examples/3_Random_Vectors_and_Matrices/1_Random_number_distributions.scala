import breeze.stats.distributions._
import breeze.linalg._
import breeze.numerics._ 

val uniformDist = Uniform(0,1)
println("\nUniform Dist:" +uniformDist.sample(3))

val gaussianDist = Gaussian(5,1) //mean of 5 and standard deviation of 1

println("\nGaussian Dist:" +gaussianDist.sample(3))

val poissonDist = Poisson(5) //mean of 5
println("\nPoisson Dist:" +poissonDist.sample(3))
