val df = spark.read.
  format("csv").
  option("header", "true").
  option("inferschema", "true").
  option("delimiter",";").
  load("winequality-red.csv")

//Summary

df.printSchema

df.select("quality").describe().show()

df.select("quality").count

df.select(count("quality")).show()

df.select(mean("quality")).show()

df.select(stddev("quality")).show()

df.select(max("quality")).show()

df.select(min("quality")).show()

df.select(sum("quality")).show()

df.select(mean("quality"),max("quality"),min("quality")).show()

//Covariance(x,y) = sum((x_i-<x>)*(y_i-<y>))/(n-1)
//Correlation(x,y) = sum((x_i-<x>)*(y_i-<y>))/sqrt(sum((x_i-<x>)**2)*sum((y_i-<y>)**2))

println("Covariance:")
df.stat.cov("quality", "density")

println("Correlation:")
df.stat.corr("quality", "density")

//Frequency
df.groupBy("quality").count().show()

df.groupBy("quality").count().select(col("quality"),(col("count")/df.count).as("frequency")).show()

//Cross Tabulation
val names = List("Alice", "Bob", "Mike")
val items = List("milk", "bread", "butter", "apples", "oranges")

val df2 = List.range(0,100).map(i => (names(i % 3),items(i % 5)) ).toDF("name", "item")
df2.show(20)

df2.stat.crosstab("name", "item").show()

//Function on all columns
val df3 = df2.stat.crosstab("name", "item").drop("name_item")
df3.select(df3.columns.map(cos(_)) :_*).show()