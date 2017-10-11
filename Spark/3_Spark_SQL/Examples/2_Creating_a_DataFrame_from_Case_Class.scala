case class Customer(Id: Int, name: String, age: Int, gender: String)

val customers = List(Customer(1, "James", 21, "M"),
                     Customer(2, "Liz", 25, "F"),
                     Customer(3, "John", 31, "M"),
                     Customer(4, "Jennifer", 45, "F"),
                     Customer(5, "Robert", 41, "M"),
                     Customer(6, "Sandra", 45, "F")
                    )

val df = spark.createDataFrame(customers)
df.printSchema
df.show()

val df2 = customers.toDF
df2.printSchema
df2.show()




