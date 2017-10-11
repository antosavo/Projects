import breeze.linalg._

val v = DenseVector.range(0, 5, 1)

val w = DenseVector.fill(5, 2)

println("v dot w = " +(v.dot(w))) //both Int

println("v dot w = " +(v dot w))
