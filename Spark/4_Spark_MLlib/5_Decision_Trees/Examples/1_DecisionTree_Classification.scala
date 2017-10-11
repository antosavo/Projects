import org.apache.spark.ml.classification.DecisionTreeClassifier
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.feature.{VectorAssembler,StringIndexer,IndexToString}
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator

//Explain Decision Tree Classifier:
println("Decision Tree Classifier:\n")
println((new DecisionTreeClassifier().explainParams)+"\n")

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

val dfv = assembler.transform(df)

dfv.show()

/*
//String Indexer
val labelToDouble = udf((x: String) => {
	if (x == "virginica") 0.0
	else if (x == "versicolor") 2.0
	else 3.0
	}) 

val dfv = assembler.transform(df).select(labelToDouble(col("species")).as("label"), col("features"))
*/

//String Indexer
val indexer = new StringIndexer().
  setInputCol("species").
  setOutputCol("label").
  fit(df)
    
val dfi = indexer.transform(dfv).select("features","label","species")

dfi.show()

//Split the data into training and test sets (30% held out for testing).
val Array(trainingData, testData) = dfi.randomSplit(Array(0.7, 0.3))

//Train a DecisionTree model.
val dt = new DecisionTreeClassifier().setMaxDepth(3)

//Train model
val model = dt.fit(trainingData)

//Make predictions
val predictions = model.transform(testData)
predictions.show()

//Convert indexed labels back to original labels.
val labelConverter = new IndexToString().
  setInputCol("prediction").
  setOutputCol("predictedLabel").
  setLabels(indexer.labels)

val labeledPredictions = labelConverter.transform(predictions)
labeledPredictions.show()

//Evaluator
val evaluator = new MulticlassClassificationEvaluator().
  setMetricName("accuracy")
    
val accuracy = evaluator.evaluate(labeledPredictions)
println("Accuracy = " + accuracy)