val df = List(
           ("red", 12, 13, 14, 15),
           ("blue", 4, 5, 6, 7),
           ("blue", 3, 9, 5, 8),
           ("yellow", 8, 9, 10, 11),
           ("white", 0, 1, 2, 3)).toDF("color","ball", "pen", "pencil", "paper")
df.printSchema
df.show()

df.sort("color").show()

df.sort(col("ball").desc).show()

df.sort(col("color"),col("pen").desc).show()

df.orderBy(col("color").desc, col("pen").asc).show()//orderBy = sort
