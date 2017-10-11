import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.ml.evaluation.RegressionEvaluator
import breeze.plot._

//DataFrame

val df = spark.read.
    format("csv").
    option("header", "true").
    option("inferschema", "true").
    option("delimiter",";").
    load("winequality-red.csv")

df.show(10)

df.printSchema

println("\nColumn Names:")//df.columns is an array
df.columns.foreach(println)

println("\nNumber Columns:" + df.columns.length)

println("\nNumber Rows:" + df.count)

println("\nMean for Classes:\n")
df.groupBy("quality").mean().show()

println("\nCorrelation quality-\n")
for(a <- df.columns) println(a + ":" + df.stat.corr("quality", a))

//Transform features to dense vector

//val features = df.columns.slice(0, df.columns.length -1)
val features = Array("volatile acidity", "citric acid", "sulphates", "alcohol")

//println("features:" + features)

val assembler = new VectorAssembler().
  setInputCols(features).//setInputCols(Array("_c1", "_c2")).
  setOutputCol("features")

val dfv = assembler.transform(df).select(col("quality").cast("Double"), col("features"))

dfv.show()

//Split data into training (60%) and test (40%).

val Array(training, test) = dfv.randomSplit(Array(0.75, 0.25))

//Fit training set

val lr = new LinearRegression().
  setMaxIter(100).
  setElasticNetParam(1.0).
  setLabelCol("quality").//by default input columns: label and features
  setFeaturesCol("features")
  //setStandardization("true")

val model = lr.fit(training)

println("NumIterations:" + model.summary.totalIterations)

println("Coefficients:" + model.coefficients)

println("Intercept:" + model.intercept)

println("r2 training:" + model.summary.r2)

//Calculate r2 score using evaluetor

val predictions = model.transform(test)

println("Predictions test:")
predictions.show()

val evaluator = new RegressionEvaluator().setMetricName("r2").
  setLabelCol("quality").
  setPredictionCol("prediction")
  
val score = evaluator.evaluate(predictions)

println("r2 = " + score)


//Plot
val fig = Figure()
val plt = fig.subplot(0)

val x = predictions.select("quality").as[Double].collect

val y = predictions.select("prediction").as[Double].collect

plt += plot(x, y, '+', name = "Data", colorcode="red")
plt += plot(Array(2.0,9.0), Array(2.0,9.0), '-', name = "l=p", colorcode="blue")

plt.legend = true
plt.title = "Regression"
plt.xlabel = "label"
plt.xlim(2,9)
plt.ylabel = "prediction"
plt.ylim(2,9)

fig.saveas("Linear_Regression_Wine_B.png")