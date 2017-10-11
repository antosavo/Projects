import org.apache.spark.ml.classification.DecisionTreeClassifier
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.feature.{VectorAssembler,StringIndexer,IndexToString}
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.ml.Pipeline

//A pipeline is a set of data processing elements connected in series, where the output 
//of one element is the input of the next one

//DataFrame

val df = spark.read.
  format("csv").
  option("header", "true").
  option("inferschema", "true").
  option("delimiter",",").
  load("Iris.csv")

df.printSchema

df.show()

println("\nColumn Names:")//df.columns is an array
df.columns.foreach(println)

println("\nNumber Columns:" + df.columns.length)

println("\nNumber Rows:" + df.count)

println("\nDistinct species:")
df.select("species").distinct.collect.foreach(println)

println("\nFrequency species:")
df.groupBy("species").count.select(col("species"),(col("count")/df.count).as("frequency")).show()

//Vectorize features
val features = df.columns.slice(0, df.columns.length -1)

println("features:" + features)

val assembler = new VectorAssembler().
  setInputCols(features).//setInputCols(Array("_c1", "_c2")).
  setOutputCol("features")

//String Indexer
val indexer = new StringIndexer().
  setInputCol("species").
  setOutputCol("label")

//Pipeline
val pipeline = new Pipeline().
  setStages(Array(assembler, indexer))

val dfi = pipeline.fit(df).transform(df).select("features","label")

dfi.show()

//Split the data into training and test sets (30% held out for testing).
val Array(trainingData, testData) = dfi.randomSplit(Array(0.7, 0.3))

//Train a DecisionTree model.
val dt = new DecisionTreeClassifier()

//Train model
val model = dt.fit(trainingData)

//Make predictions
val predictions = model.transform(testData)
predictions.show()

//Evaluator
val evaluator = new MulticlassClassificationEvaluator().
  setMetricName("accuracy")
    
val accuracy = evaluator.evaluate(predictions)
println("Accuracy = " + accuracy)