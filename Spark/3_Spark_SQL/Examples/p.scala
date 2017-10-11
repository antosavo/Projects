import org.apache.spark.sql.functions

val L = List((1,4),(2,5))

val df = sqlContext.createDataFrame(L)
df.printSchema
df.show()
df.describe().show()

val df2 = df.withColumn("newName", lit(0))
df2.printSchema
df2.show()

val df3 = df.withColumn("sin(1)",sin("_1"))
df3.printSchema
df3.show()

val df4 = df.select(df("_1"),df("_2"),df("_1")+ df("_2")).toDF("A","B","C")
df4.printSchema
df4.show()

val df5 = sqlContext.range(0, 10)
df5.show()

df5.select(df5("id"), rand(seed=10).alias("uniform"), randn(seed=27).alias("normal")).show()

val df6 = df.select(df("_1"),df("_2"),rand(10)).toDF("A","B","C")
df6.printSchema
df6.show()

