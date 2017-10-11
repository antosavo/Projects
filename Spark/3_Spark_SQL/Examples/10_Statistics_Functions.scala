val df = spark.range(0, 5).withColumn("uniform", rand()).withColumn("normal", randn())
df.show()

df.printSchema

df.count

df.describe().show()

df.describe("uniform","normal").show()

df.select(df("uniform")).describe().show()

df.select("uniform").count

df.select(count("uniform")).collect

df.select(mean("uniform")).collect

df.select(stddev("uniform")).collect

df.select(max("uniform")).collect

df.select(min("uniform")).collect

df.select(sum("uniform")).collect

df.select(sin("uniform")).collect

df.select(mean("uniform"),max("uniform"),min("uniform")).show()

df.stat.cov("uniform", "normal")  //Covariance(x,y) = sum((x_i-<x>)*(y_i-<y>))/(n-1)

df.stat.corr("uniform", "normal") //Correlation(x,y) = sum((x_i-<x>)*(y_i-<y>))/sqrt(sum((x_i-<x>)**2)*sum((y_i-<y>)**2))

df.stat.corr("id", "id")

//Cross Tabulation
val names = List("Alice", "Bob", "Mike")
val items = List("milk", "bread", "butter", "apples", "oranges")

val df2 = List.range(0,100).map(i => (names(i % 3),items(i % 5)) ).toDF("name", "item")
df2.show(20)

df2.stat.crosstab("name", "item").show()

//Frequency
df2.groupBy("item").count().show()

df2.groupBy("item").count().select(col("item"),(col("count")/df2.count).as("frequency")).show()

//Function on all columns
val df3 = df2.stat.crosstab("name", "item").drop("name_item")
df3.select(df3.columns.map(cos(_)) :_*).show()







