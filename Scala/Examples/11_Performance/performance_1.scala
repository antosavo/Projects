import breeze.linalg._

val v = DenseVector.fill(4000, 2.0)
var w = DenseVector.fill(4000,0.0)
val I = DenseMatrix.eye[Double](4000)

//println("v=" +v)
//println("w=" +w)
//println("I=" +I)

println("Time breeze:")

val start = System.nanoTime
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 

w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
w = I*v 
val end = System.nanoTime

val t = (end - start)/1e9
    
println(t)
      



