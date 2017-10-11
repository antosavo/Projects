import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.ml.evaluation.RegressionEvaluator

//Read file

val df = spark.read.
    format("csv").
    option("inferschema", "true").
    option("delimiter"," ").
    load("data_1.txt")

df.show()

//Transform features to dense vector

val Columns = df.columns
val Columns12 = df.columns.slice(1, 3)

val assembler = new VectorAssembler().
  setInputCols(Columns12).//setInputCols(Array("_c1", "_c2")).
  setOutputCol("features")

val dfv = assembler.transform(df).select(col("_c0").cast("Double").as("label"), col("features"))

dfv.show()

//Split data into training (60%) and test (40%).

val Array(training, test) = dfv.randomSplit(Array(0.6, 0.4))

//Fit training set

val lr = new LinearRegression().
  setMaxIter(100).
  setElasticNetParam(1.0)
//setStandardization("true")

val model = lr.fit(training)

println("NumIterations:" + model.summary.totalIterations)

println("Coefficients:" + model.coefficients)

println("Intercept:" + model.intercept)

println("Predictions training:")
model.transform(training).show()

println("r2 training:" + model.summary.r2)

//Calculate r2 score using evaluetor

val predictions = model.transform(test)

val evaluator = new RegressionEvaluator().setMetricName("r2")
//by default the metric is "rmse": root mean squared error
//by default input columns: prediction and label
//setLabelCol("label").
//setPredictionCol("prediction").
  
val score = evaluator.evaluate(predictions)

println("r2 = " + score)

//Calculate r2 score by hand

val mean_l = predictions.select(mean("label")).take(1)(0)(0).toString.toDouble

val R2 = predictions.select(lit(1)-(sum(pow(col("label")-col("prediction"),2))/sum(pow(col("label")-mean_l,2)))).take(1)(0)(0).toString.toDouble

println("R2 = " + R2)


