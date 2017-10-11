import breeze.linalg._

val v = DenseVector(1,2,3,4,5)
println("v = " +v)

val sparse = SparseVector(0.0, 1.0, 0.0, 2.0, 0.0)
println ("u = " +sparse)