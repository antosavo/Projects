//Red Wine
val df1 = spark.read.
  format("csv").
  option("header", "true").
  option("inferschema", "true").
  option("delimiter",";").
  load("winequality-red.csv")

df1.show(10)

df1.printSchema

println("\nColumn Names:")
df1.columns.foreach(println)

println("\nNumber Columns:" + df1.columns.length)

println("\nNumber Rows:" + df1.count)

println("\nDistinct Quality:")
df1.select("quality").distinct.collect

df1.describe("quality").show()

df1.select(mean("quality"),max("quality"),min("quality")).show()

df1.select("quality").filter(col("quality")>=5).show()

println("\nMean for Classes:\n")
df1.groupBy("quality").mean().show()

println("\nCorrelation quality-\n")
for(a <- df1.columns) println(a + ":" + df1.stat.corr("quality", a))

//White Wine
val df2 = spark.read.
  format("csv").
  option("header", "true").
  option("inferschema", "true").
  option("delimiter",";").
  load("winequality-white.csv")

//

val df = df1.unionAll(df2)
df.show(10)

//df.toJSON.first()

df.repartition(1).write.format("csv").option("header", "true").mode("overwrite").save("wine-data")