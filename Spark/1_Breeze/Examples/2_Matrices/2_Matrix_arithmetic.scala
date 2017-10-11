import breeze.linalg._
import breeze.numerics._ //for functions sin, log
import breeze.stats._ //for stsistics

val M = DenseMatrix((1,2,3),(11,12,13),(21,22,23))
println("\nM : \n" + M)

val I = DenseMatrix.eye[Int](3)
println("\nI : \n" + I)

val A = M + I
println("\nM + I: \n" + A)

val B = M*I
println("\nM * I: \n" + B)

val C = 2*I
println("\n2 * I: \n" + C)

val D = I + 2
println("\nI+2: \n" + D)

val E = M :* I
println("\nElement by element M:*I : \n" + E)


