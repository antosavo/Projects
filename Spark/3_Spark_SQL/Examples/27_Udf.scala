val df = List((1,"Red"), (2,"Green"), (3,"Blue")).toDF("id","color")
df.show()

// Define the UDF
val isGreen = udf((color: String) => {
	if (color == "Green") 1
	else 0
	})

val df1 = df.withColumn("Green_Ind", isGreen(col("color")))
df1.show()