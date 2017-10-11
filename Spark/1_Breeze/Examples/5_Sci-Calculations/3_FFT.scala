import breeze.linalg._
import scala.math.{sin, Pi}
import breeze.math.Complex
import breeze.signal._
import breeze.plot._

val y = DenseVector.tabulate(256){i => Complex(sin(i), 0.0)}

val f = Figure()
val p = f.subplot(0)
val x = linspace(0.0, 256.0, 256)

val transformed = fourierTr(y)

val inverse = iFourierTr(transformed)

val freq = fourierFreq( 256, dt = 1)

p += plot(freq, transformed.map(j => j.abs))
p.xlabel = "freq"
p.ylabel = "amplitude"

//p.setXAxisIntegerTickUnits()
p.setXAxisDecimalTickUnits()

f.saveas("transformed.png")

