val df = spark.read.
  format("csv").
  option("header", "true").
  option("inferschema", "true").
  option("delimiter",";").
  load("winequality-red.csv")

df.printSchema

df.show()

println("Total number of instances =" + df.count)

val dfs = df.sample(false, 0.1) //no replacement (false), 0.1 % sampling 

println("Number of instances in sample =" + dfs.count)

val dfArray = df.randomSplit(Array(0.6, 0.2, 0.2))

println("Elements in df_0: " + dfArray(0).count)
dfArray(0).show(5)

println("Elements in df_1: " + dfArray(1).count)
dfArray(1).show(5)

println("Elements in df_2: " + dfArray(2).count)
dfArray(2).show(5)