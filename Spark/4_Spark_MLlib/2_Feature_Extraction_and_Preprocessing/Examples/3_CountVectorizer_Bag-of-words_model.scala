import org.apache.spark.ml.feature.CountVectorizer
import org.apache.spark.ml.linalg.Vector
//import org.apache.spark.ml.linalg.DenseVector


val df = spark.createDataFrame(Seq(
  (0, Array("ant", "bat", "cat", "dog", "eel")),
  (1, Array("dog","bat", "ant", "bat", "cat"))
)).toDF("id", "words")

// fit a CountVectorizerModel from the corpus
val CV = new CountVectorizer().
  setInputCol("words").
  setOutputCol("features")
  //setVocabSize(3)
  
val cvModel = CV.fit(df)

println("vocabulary:")
cvModel.vocabulary

//feature(number of words, simbols, frequency)
val cvDF = cvModel.transform(df)
cvDF.show()

cvDF.select("features").collect.map(row => row(0).asInstanceOf[Vector].toDense)
