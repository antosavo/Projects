import  java.io._
import breeze.linalg._

val M = csvread(file = new File("Data.csv"), separator='\t', skipLines=1)
println ("Usage matrix :\n"+ M(0 to 5,::))
println ("\nCols M = "+ M.cols)
println ("\nRows M = "+ M.rows)

val x = M(::,0)
println ("\nx = " +x )

val y = M(::,1)
println ("\ny = " +y )

val z = M(::,2)
println ("\nz = " +z )

val N = DenseVector.horzcat(x,y)

csvwrite(file = new File("Output.csv"), mat = N, separator =',')
