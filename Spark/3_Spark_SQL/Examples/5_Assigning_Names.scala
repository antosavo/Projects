val L = List((1,"Android"), (2, "iPhone"), (3, "iPhone"))

val df = spark.createDataFrame(L).toDF("id", "type")
df.columns.foreach(println)
df.show()

val df2 = df.withColumnRenamed("id", "position") //id => position
df2.show()

val NewColumns = df.columns.map(name => df(name).as(name+"_1"))
val df3 = df.select(NewColumns : _*)
df3.show()




