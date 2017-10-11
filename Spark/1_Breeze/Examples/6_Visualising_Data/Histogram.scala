//import breeze.linalg._
import breeze.plot._
//import breeze.numerics._

val r = scala.util.Random

val x = Array.range(0,100).map(i => r.nextDouble)


val fig = Figure()
val plt = fig.subplot(0)

//rv.setBackgroundPaint(Color.white)

plt += hist(x,10)
plt.legend = true
plt.title = "Histogram"
plt.xlabel = "x axis"
//plt.xlim(-math.Pi,math.Pi)
plt.ylabel = "y axis"
//plt.ylim(-1.2,1.2)
fig.saveas("Hist.png")