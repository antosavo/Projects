import breeze.linalg._

val M = DenseMatrix((4.0,7.0),(3.0,-5.0))
println("\nM:\n" +M)

val M_t = M.t
println("\nM_t:\n" +M_t)

val M_i = inv(M)
println("\nM_i:\n" +M_i)

println("\nM_i*M:\n" +(M_i*M))