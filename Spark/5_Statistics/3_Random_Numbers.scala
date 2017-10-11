val df = spark.range(0, 5).withColumn("uniform", rand()).withColumn("normal", randn())
df.show()

df.printSchema

val r = scala.util.Random

//Uniform distribution 0 to 1
val Uniform = Array.range(0,10).map(i => r.nextDouble)

//Normal distribution avg 0 stddev 1
val Normal = Array.range(0,10).map(i => r.nextGaussian)