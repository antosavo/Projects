import breeze.linalg._
import breeze.stats._
import breeze.numerics._

val M = DenseMatrix((4.0,7.0),(3.0,-5.0))
println("\nM:\n" +M)

println("\neigvalues(M)=" +eig(M).eigenvalues)

val e1 = eig(M).eigenvalues(0)

val e2 = eig(M).eigenvalues(1)

println("\neigvectors(M):\n" +eig(M).eigenvectors)

val v1 = eig(M).eigenvectors(::,0)
println("\neigvector(M)_1=" +v1)
println("\nM*v1=" +(M*v1))
println("\ne1*v1=" +(e1*v1))

val v2 = eig(M).eigenvectors(::,1)
println("\neigvector(M)_2=" +v2)
println("\nM*v2=" +(M*v2))
println("\ne2*v2=" +(e2*v2))



