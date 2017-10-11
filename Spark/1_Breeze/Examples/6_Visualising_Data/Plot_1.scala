import breeze.linalg._
import breeze.plot._
import breeze.numerics._

val x = linspace(-math.Pi, math.Pi, 30)
val fx = sin(x)
val gx = cos(x)

val fig = Figure()
val plt = fig.subplot(0)

//rv.setBackgroundPaint(Color.white)

plt += plot(x, fx, name = "sin(x)", colorcode="red")
plt += plot(x, gx, '+', name = "cos(x)", colorcode="black")
plt.legend = true
plt.title = "Sin function"
plt.xlabel = "x axis"
plt.xlim(-math.Pi,math.Pi)
plt.ylabel = "y axis"
plt.ylim(-1.2,1.2)
fig.saveas("sin.png")

//fig.refresh()