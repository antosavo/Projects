val df = spark.read.
    format("csv").
    option("inferschema", "true").
    option("delimiter"," ").
    load("data_1.txt")

df.show()
