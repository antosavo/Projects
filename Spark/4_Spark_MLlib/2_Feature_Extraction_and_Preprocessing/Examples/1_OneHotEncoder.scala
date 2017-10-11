import org.apache.spark.ml.feature.{OneHotEncoder, StringIndexer}
import org.apache.spark.ml.linalg.Vector
//import org.apache.spark.ml.linalg.DenseVector

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

val encoder = new OneHotEncoder().
  setInputCol("categoryIndex").
  setOutputCol("categoryVec")
    
val encoded = encoder.transform(indexed)
    
encoded.show()

encoded.select("categoryVec").collect.map(row => row(0).asInstanceOf[Vector].toDense)
