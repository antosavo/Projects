import breeze.linalg._
import breeze.numerics._ //for functions sin, log
import breeze.stats._ //for stsistics

val M = DenseMatrix((1,2,3),(11,12,13),(21,22,23))
println("\nM : \n" + M)

val I = DenseMatrix.eye[Int](3)
println("\nI : \n" + I)

val C = DenseMatrix.vertcat(I, M)
println("\nVertically concat(I,M) : \n" + C)
