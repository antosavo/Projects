import org.apache.spark.ml.feature.{RegexTokenizer, Tokenizer}
import org.apache.spark.sql.SparkSession
//import org.apache.spark.ml.linalg.Vector


val sentenceDataFrame = spark.createDataFrame(Seq(
  (0, "Hi I heard about Spark"),
  (1, "I wish Java could use case classes"),
  (2, "Logistic,regression,models,are,neat")
)).toDF("label", "sentence")

val tokenizer = new Tokenizer().
  setInputCol("sentence").
  setOutputCol("words")

val regexTokenizer = new RegexTokenizer().
  setInputCol("sentence").
  setOutputCol("words").
  setPattern("\\W") // alternatively .setPattern("\\w+").setGaps(false)

val tokenized = tokenizer.transform(sentenceDataFrame)
tokenized.show()
tokenized.select("words").collect.map(i => i(0))

val regexTokenized = regexTokenizer.transform(sentenceDataFrame)
regexTokenized.show()
regexTokenized.select("words").collect.map(i => i(0))