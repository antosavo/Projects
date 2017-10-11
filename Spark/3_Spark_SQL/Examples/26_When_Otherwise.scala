
val df = List((1,"Red"), (2,"Green"), (3,"Blue")).toDF("id","color")
df.show()

val df1 = df.withColumn("Green_Ind", when(col("color") === "Green", 1).otherwise(0) )
df1.show()