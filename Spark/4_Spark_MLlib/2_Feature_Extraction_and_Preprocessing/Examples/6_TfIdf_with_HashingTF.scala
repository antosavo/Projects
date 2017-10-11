import org.apache.spark.ml.feature.{HashingTF, IDF, Tokenizer}
import org.apache.spark.ml.linalg.Vector

val sentenceData = spark.createDataFrame(Seq(
  (0, "Hi I heard about Spark"),
  (0, "I wish Java could use case classes"),
  (1, "Logistic regression models are neat")
)).toDF("label", "sentence")

//

val tokenizer = new Tokenizer().
  setInputCol("sentence").
  setOutputCol("words")

val wordsData = tokenizer.transform(sentenceData)

wordsData.show()

//

val hashingTF = new HashingTF().
  setInputCol("words").
  setOutputCol("rawFeatures").
  setNumFeatures(20)

val featurizedData = hashingTF.transform(wordsData)
    // alternatively, CountVectorizer can also be used to get term frequency vectors

featurizedData.show()

featurizedData.select("rawFeatures").collect.map(row => row(0).asInstanceOf[Vector].toDense)

//

val idf = new IDF().
  setInputCol("rawFeatures").
  setOutputCol("features")

val idfModel = idf.fit(featurizedData)
val rescaledData = idfModel.transform(featurizedData)

rescaledData.show()

rescaledData.select("features").collect.map(row => row(0).asInstanceOf[Vector].toDense)