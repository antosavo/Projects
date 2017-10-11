import breeze.linalg._
import breeze.numerics._ //for functions sin, log
import breeze.stats._ //for stsistics

val M = DenseMatrix((1,2,3),(11,12,13),(21,22,23))
println("M : \n" + M)

val S = CSCMatrix((1,0,0),(11,0,0),(0,0,23)) //Breeze's Sparse matrix is a Dictionary of Keys.
println("S : \n" + S)

val Z = DenseMatrix.zeros[Double](5,4)
println("Z : \n" + Z)

val F0 = DenseMatrix.tabulate(5,4)((r,c) => r*c) //Int
println("F0 : \n" + F0)

val F1 = DenseMatrix.tabulate[Double](5,4)((r,c) => r*c)
println("F1 : \n" + F1)

val F2 = DenseMatrix.tabulate[Double](5,4)((r,c) => math.cos(r*c))
println("F2 : \n" + F2)

val I = DenseMatrix.eye[Int](3)
println("I : \n" + I)

val R = DenseMatrix.rand(3,3) //Random Matrix
println("R : \n" + R)

val A1 = new DenseMatrix(2,2,Array(2,3,4,5))
println("A1 : \n" + A1)

val A2 = new DenseMatrix(2,2,Array(2,3,4,5,6,7))
println("A2 : \n" + A2)



