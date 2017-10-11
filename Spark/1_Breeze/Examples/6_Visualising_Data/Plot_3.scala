import breeze.plot._

val f = Figure()
val plt = f.subplot(0)

val x = Array.range(1,10,2)
val y = x.map(i => i*i)

plt += plot(x, y, name="Line", colorcode="red")

plt += plot(x, y, style='.' , name="Points", colorcode="blue")

//style='+','.','-'

//val l= List("A","B","C","D","E")

//plt += plot(x, y, style='+' , name="Points", colorcode="blue", labels = Array.range(0,5).map(i=>l(i)))

plt.xlim(0,10)
plt.ylim(0,100)

plt.xlabel = "x axis"
plt.ylabel = "y axis"

plt.legend = true

//plt.logScaleX = true
//plt.logScaleY = true

//plt.setXAxisIntegerTickUnits()
//plt.setXAxisDecimalTickUnits()

plt.title = "My Plot"

f.saveas("lines.png")

//f.clear