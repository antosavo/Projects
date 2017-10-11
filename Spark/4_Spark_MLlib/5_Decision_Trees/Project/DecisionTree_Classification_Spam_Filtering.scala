import org.apache.spark.ml.classification.DecisionTreeClassifier
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.ml.feature.{Tokenizer, StopWordsRemover, CountVectorizer, StringIndexer}
import org.apache.spark.ml.Pipeline
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object DecisionTree_Classification
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
    load("SMSSpamCollection.dat").toDF("label_name","sentences")

df.show()

println("\nNumber Rows:" + df.count)
println("\nNumber ham messages:" + df.filter(col("label_name")==="ham").count)
println("\nNumber spam messages:" + df.filter(col("label_name")==="spam").count)

//Tokenizer
val tokenizer = new Tokenizer().
    setInputCol("sentences").
    setOutputCol("words")

//Stop Words Remover
val remover = new StopWordsRemover().
    setInputCol("words").
    setOutputCol("filteredWords")

//CountVectorizer
val CV = new CountVectorizer().
    setInputCol("filteredWords").
    setOutputCol("features")

//String Indexer
val indexer = new StringIndexer().
  setInputCol("label_name").
  setOutputCol("label")

//Pipeline
val pipeline = new Pipeline().
  setStages(Array(tokenizer, remover, CV, indexer))

val dfi = pipeline.fit(df).transform(df).select("features","label")

dfi.show()

//Split training, test data
val Array(trainingData, testData) = dfi.randomSplit(Array(0.7, 0.3))

//Train a DecisionTree model.
val dt = new DecisionTreeClassifier().setMaxDepth(3)

//Train model
val model = dt.fit(trainingData)

//Make predictions
val predictions = model.transform(testData)
predictions.show()

predictions.write.format("json").mode("overwrite").save("Model_Predictions")

//Evaluator
val evaluator = new MulticlassClassificationEvaluator().
  setMetricName("accuracy")
    
val accuracy = evaluator.evaluate(predictions)
println("Accuracy = " + accuracy)

List(accuracy).toDF.repartition(1).write.format("csv").mode("overwrite").save("Model_accuracy")

//Crosstabulation
println("Crosstabulation:")
predictions.stat.crosstab("label", "prediction").show()

spark.stop()

}

}