val L = List((1,"blue","ball",1.2), 
             (2, "green","pen",1.0), 
             (3, "yellow","pencil",0.6),
             (4,"red","paper",0.9)
            )

val df = L.toDF("id","color","object","price")
df.printSchema
df.show()

//Add Columns

val df2 = df.withColumn("zeros", lit(0))
df2.show()

val df3 = df.withColumn("ones", lit(1))
df3.show()

val df4 = df.withColumn("uniform", rand()).withColumn("normal", randn())
df4.show()

val df5 = df.withColumn("range", df("id")-1)
df5.show()

val df6 = df.withColumn("sin(id)", sin(df("id")))
df6.show()

val df7 = df.withColumn("id double", df("id").cast("double")).drop("id")
df7.show()

//Add Row

val NewRow = List((5,"white","mug",1.7)).toDF()

val df8 = df.unionAll(NewRow)
df8.show()

//Update value

val df9 = df8.withColumn("update price", when(df8("price")===0.9, 1.9).
                        otherwise(df8("price")) ).drop("price")
df9.show()

df.na.replace("price", Map(0.9 -> 5.9)).show()
df.show()

