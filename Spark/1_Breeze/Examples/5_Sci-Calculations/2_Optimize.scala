import breeze.linalg._
import scala.math.{pow}
import breeze.optimize._

def F(x:Double, y:Double, z:Double) = pow(x + 1.0, 2.0) + pow(y - 2.0, 2.0) + pow(z + 4.0, 2.0)

def Grad_F(x:Double, y:Double, z:Double) = DenseVector(2.0 * (x + 1), 2.0 * (y - 2.0), 2.0 * (z + 4.0))


val fn = new DiffFunction[DenseVector[Double]] {
    def calculate(x: DenseVector[Double]) = (F(x(0),x(1),x(2)),Grad_F(x(0),x(1),x(2)))
}


val lbfgs = new LBFGS[DenseVector[Double]](maxIter=100, m=10, tolerance=0.001)

val solution = lbfgs.minimize(fn, DenseVector(0.0, 0.0, 0.0))

println("solution: "+solution)
