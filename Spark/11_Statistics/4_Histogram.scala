import breeze.plot._

//RDD Histogram
val myRDD = sc.parallelize(Array(0,12,34,67,55,28,90,99,12,3,56,74,44,87,23,49,89,87,98,100))

myRDD.histogram(4) //4 spaced buckets, between myRDD.min ->  myRDD.max 

myRDD.histogram(Array(0.0, 33.3, 66.6, 100.0))

//DF Histogram
val r = scala.util.Random

val df = List.range(0,100).map(i => (i, r.nextDouble)).toDF("range","rand uniform")
df.show()

df.select("rand uniform").as[Double].rdd.histogram(5)

df.select("rand uniform").as[Double].rdd.histogram(Array(0.00, 0.20, 0.40, 0.60, 0.80, 1.00))

//Plot

val x = df.select("rand uniform").as[Double].collect

val fig = Figure()
val plt = fig.subplot(0)

plt += hist(x,5)
plt.legend = true
plt.title = "Histogram"
plt.xlabel = "x axis"
//plt.xlim(-math.Pi,math.Pi)
plt.ylabel = "y axis"
//plt.ylim(-1.2,1.2)
fig.saveas("Histogram.png")