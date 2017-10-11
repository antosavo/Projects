import breeze.linalg._
import scala.math._

val v = DenseVector.tabulate[Double](5)(i => i*i)
println("v = " +v)

val w = DenseVector.tabulate[Double](5)(i => cos(i))
println("w = " +w)