import org.apache.spark.ml.classification.NaiveBayes
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.ml.feature.{Tokenizer, StopWordsRemover, CountVectorizer}
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object Naive_Bayes_Classiﬁcation
{

def main(args: Array[String]) 
{

val spark = SparkSession.
  builder.
  appName("MyApp").
  getOrCreate()
  //config("spark.sql.caseSensitive", "true").
import spark.implicits._

//DataFrame

val df = spark.read.
    format("csv").
    option("header", "false").
    option("inferschema", "true").
    option("delimiter","\t").
    load("SMSSpamCollection.dat").toDF("label","sentences")

df.show()

println("\nNumber Rows:" + df.count)
println("\nNumber ham messages:" + df.filter(col("label")==="ham").count)
println("\nNumber spam messages:" + df.filter(col("label")==="spam").count)

//Tokenizer

val tokenizer = new Tokenizer().
    setInputCol("sentences").
    setOutputCol("words")

val wordsData = tokenizer.transform(df)

wordsData.show()

//Stop Words Remover

val remover = new StopWordsRemover().
    setInputCol("words").
    setOutputCol("filteredWords")

val stopWordsData = remover.transform(wordsData)

stopWordsData.show()

//Label to Double

val labelToDouble = udf((x: String) => {
	if (x == "ham") 1.0
	else 0.0
	}) 

//CountVectorizer

val CV = new CountVectorizer().
    setInputCol("filteredWords").
    setOutputCol("features")

val cvModel = CV.fit(stopWordsData)

val vdf = cvModel.transform(stopWordsData).
    select(labelToDouble(col("label")).as("label"),col("features"))

vdf.show()

//Split training, test data
val Array(trainingData, testData) = vdf.randomSplit(Array(0.7, 0.3))

//Train a NaiveBayes model
val model = new NaiveBayes().setModelType("multinomial").
    fit(trainingData)

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
