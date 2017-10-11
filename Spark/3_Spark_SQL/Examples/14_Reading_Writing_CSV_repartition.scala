val df = spark.read.
  format("csv").
  option("header", "true").
  option("delimiter","|").
  load("StudentData.csv")

val df2 = df.select("studentName","email").repartition(1) //new df with 1 partition

df2.write.
  format("csv").
  mode("overwrite").
  save("StudentData")

df2.write.
  format("json").
  mode("overwrite").
  save("StudentData_JSON")

//df2.write.mode("overwrite").saveAsTable("table") //Hive table


