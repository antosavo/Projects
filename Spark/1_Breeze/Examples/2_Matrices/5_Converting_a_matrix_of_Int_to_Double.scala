import breeze.linalg._
import breeze.numerics._ //for functions sin, log
import breeze.stats._ //for stsistics

val M = DenseMatrix((1,2,3),(11,12,13),(21,22,23))
println("\nM : \n" + M)

val N = convert(M, Double)
println("\nM to Double : \n" + N)
