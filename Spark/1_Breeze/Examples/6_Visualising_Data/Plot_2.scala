import breeze.plot._

val f = Figure()
val plt = f.subplot(0)

val x = Array.range(1,10,2)
val y = x.map(i => i*i)

plt += scatter(x, y, size = x.map(i=>0.25), colors = x.map(i=> java.awt.Color.red))

plt.xlim(0,10)
plt.ylim(0,100)

plt.xlabel = "x axis"
plt.ylabel = "y axis"

//plt.legend = true

//plt.logScaleX = true
//plt.logScaleY = true

//plt.setXAxisIntegerTickUnits()
//plt.setXAxisDecimalTickUnits()

plt.title = "My Plot"

f.saveas("Scatter.png")

//f.clear