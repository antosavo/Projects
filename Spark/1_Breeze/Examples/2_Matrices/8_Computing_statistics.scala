import breeze.linalg._
import breeze.stats._
import breeze.numerics._

val M = DenseMatrix((4.0,7.0),(3.0,-5.0))
println("\nM:\n" +M)

println("\nmean(M)=" +mean(M))

println("\nstddev(M)=" +stddev(M))

println("\nmax(M)=" +max(M))

println("\nmin(M)=" +min(M))

println("\nsum(M)=" +sum(M))

println("\ncos(M):\n" +cos(M))

println("\nlog(M):\n" +log(M))

