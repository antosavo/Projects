import org.apache.spark.ml.feature.StopWordsRemover
import org.apache.spark.sql.SparkSession

val remover = new StopWordsRemover().
  setInputCol("raw").
  setOutputCol("filtered")

val dataSet = spark.createDataFrame(Seq(
  (0, Seq("I", "saw", "the", "red", "baloon")),
  (1, Seq("Mary", "had", "a", "little", "lamb"))
)).toDF("id", "raw")

remover.transform(dataSet).show()



