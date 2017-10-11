import org.apache.spark.ml.feature.StringIndexer

val df = spark.createDataFrame(Seq(
  (0, "red"),
  (1, "blue"),
  (2, "green"),
  (3, "red"),
  (4, "red"),
  (5, "green")
)).toDF("id", "category")

val indexer = new StringIndexer().
  setInputCol("category").
  setOutputCol("categoryIndex").
  fit(df)
    
val indexed = indexer.transform(df)

indexed.show()
