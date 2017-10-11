import breeze.linalg._

val M = DenseMatrix((4.0,7.0),(3.0,-5.0))
println("\nM:\n" +M)

val c1 = M(::,0)
println("\nc1:" +c1) //First Column

val c2 = M(::,1)
println("\nc2:" +c2) //Second Column

val r1 = M(0,::)
println("\nr1:" +r1) //First Row

val r2 = M(1,::)
println("\nr2:" +r2) //Second Row

val m00 = M(0,0)
println("\nM(0,0):" +m00) //Second Row