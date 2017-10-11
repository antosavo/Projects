val L = List((1,"Android"), (2, "iPhone"), (3, "iPhone"))

val df = spark.createDataFrame(L).toDF("id","type")

df.printSchema

df.columns

df.show()

df.select("id").show() //columns id

df.select(col("id")).show() //columns id

df.select(df("id")).show() //columns id

df.select("type").show() //columns type

val c = df.select("type").collect //columns to array

val c2 = df.select("type").take(2) //columns to array dim 2

df.where("id = 1").show() //row id = 1

df.filter("id = 1").show() //row id = 1, filter = where

df.filter(col("id") === 1).show() //row id = 1, filter = where

df.filter("type = 'iPhone'").show() //row type = iPhone

df.filter("id = 1").select("type").show() //element (id = 1, type)

val e = df.filter("id = 1").select("type").collect //element (id = 1, type) to array




