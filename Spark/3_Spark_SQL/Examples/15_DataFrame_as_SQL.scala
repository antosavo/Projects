//import com.databricks.spark.csv._
//val df = sqlContext.csvFile(filePath="StudentData.csv", useHeader=true, delimiter='|')
val df = spark.read.
    format("csv").
    option("header", "true").
    option("delimiter","|").
    load("StudentData.csv")

//Printing the schema of the DataFrame
println("Shema:")
df.printSchema

//We can treat a DF like a relational table and use SQL to query. 

//1) Register the df DataFrame as a table with the name "students":
df.registerTempTable("students")
//2) Query it using regular SQL:
val dfFilteredBySQL = spark.sql("SELECT * FROM students WHERE studentName!='' ORDER BY email DESC")

println("Using SQL select:")
dfFilteredBySQL.show(7)





