//val conf = new SparkConf().setAppName("colRowDataFrame").setMaster("local[2]")
//val sc = new SparkContext(conf)
//val sqlContext=new SQLContext(sc)

val L = List((1,"Android"), (2, "iPhone"), (3, "iPhone"))

val df = L.toDF("id","type")
df.printSchema
df.show()

val df2 = spark.createDataFrame(L).toDF("id","type")
df2.show()

val df3 = List.range(0,10).map(i => (i, 2*i) ).toDF("x", "2x")
df3.show()

val df4 = List.range(0,10).map(i => (math.cos(i), math.sin(i))).toDF("cos(x)", "sin(x)")
df4.show()

val df5 = spark.range(0, 5)
df5.show()

val r = scala.util.Random

val df6 = List.range(0,10).map(i => (i, r.nextDouble, r.nextGaussian)).toDF("range","rand uniform", "random normal")
df6.show()

val color = List("blue","green","yellow","red","white")

val df7 = List.range(0,5).map(i => (i, color(i))).toDF("id","color")
df7.show()












