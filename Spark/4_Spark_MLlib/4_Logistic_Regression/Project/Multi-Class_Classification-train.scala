import org.apache.spark.ml.classification.{LogisticRegression, OneVsRest}
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.ml.feature.{Tokenizer, StopWordsRemover, CountVectorizer}
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object Multi_Class_Classification
{

def main(args: Array[String]) 
{

val spark = SparkSession.
  builder.
  appName("MyApp").
  getOrCreate()
  //config("spark.sql.caseSensitive", "true").
import spark.implicits._


//Dtaframe
val df = spark.read.
    format("csv").
    option("header", "true").
    option("inferschema", "true").
    option("delimiter","\t").
    load("train.tsv")//.toDF("label","sentences")

df.show()

df.printSchema

println("\nColumn Names:")//df.columns is an array
df.columns.foreach(println)

println("\nNumber Columns:" + df.columns.length)

println("\nNumber Rows:" + df.count)

println("\nDistinct Sentiments:")
df.select("Sentiment").distinct.collect.foreach(println)

println("\nFrequencySentiments:")
df.groupBy("Sentiment").count.select(col("Sentiment"),(col("count")/df.count).as("frequency")).show()

//Tokenizer
val tokenizer = new Tokenizer().
    setInputCol("Phrase").
    setOutputCol("words")

val wordsData = tokenizer.transform(df)

wordsData.show()

//Stop Words Remover
val remover = new StopWordsRemover().
    setInputCol("words").
    setOutputCol("filteredWords")

val stopWordsData = remover.transform(wordsData)

stopWordsData.show()

//CountVectorizer
val CV = new CountVectorizer().
    setInputCol("filteredWords").
    setOutputCol("features")

val cvModel = CV.fit(stopWordsData)

val vdf = cvModel.transform(stopWordsData).
    select(col("Sentiment").cast("double").as("label"),col("features"))

vdf.show()

//Split training, test data
val Array(trainingData, testData) = vdf.randomSplit(Array(0.7, 0.3))

//Train a Logistic Regression model
val lr = new LogisticRegression().setMaxIter(50)

//One Vs Rest Classifier.
val ovr = new OneVsRest().setClassifier(lr)
val model = ovr.fit(trainingData)

//Select example rows to display
val predictions = model.transform(testData)
predictions.show()

predictions.write.format("json").mode("overwrite").save("Model_Predictions")

//Evaluator
val evaluator = new MulticlassClassificationEvaluator().
    setLabelCol("label").
    setPredictionCol("prediction").
    setMetricName("accuracy")
    
val accuracy = evaluator.evaluate(predictions)
println("Accuracy: " + accuracy)

List(accuracy).toDF.repartition(1).write.format("csv").mode("overwrite").save("Model_accuracy")

//Crosstabulation
println("Crosstabulation:")
predictions.stat.crosstab("label", "prediction").show()

spark.stop()

}

}