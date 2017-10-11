import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.tuning.{CrossValidator, ParamGridBuilder}
import breeze.plot._

//DataFrame

val df = spark.read.
  format("csv").
  option("header", "true").
  option("inferschema", "true").
  option("delimiter",";").
  load("winequality-red.csv")

//df.printSchema

//Vectorize features

val features = df.columns.slice(0, df.columns.length -1)

println("features:" + features)

val assembler = new VectorAssembler().
  setInputCols(features).//setInputCols(Array("_c1", "_c2")).
  setOutputCol("features")

val dfv = assembler.transform(df).select(col("quality").cast("Double"), col("features"))

/*
df.show(10)

df.printSchema

println("\nColumn Names:")
df.columns.foreach(println)

println("\nNumber Columns:" + df.columns.length)

println("\nNumber Rows:" + df.count)

println("\nMean for Classes:\n")
df.groupBy("quality").mean().show()

println("\nCorrelation quality-\n")
for(a <- df.columns) println(a + ":" + df.stat.corr("quality", a))
*/

//Split data into training (75%) and test (25%).

val Array(training, test) = dfv.randomSplit(Array(0.75, 0.25))

//Model Selection with cros validation

val lr = new LinearRegression().
  setMaxIter(100).//setElasticNetParam(1.0).
  setLabelCol("quality")//by default input columns: label and features
  //setFeaturesCol("features")

val evaluator = new RegressionEvaluator().setMetricName("r2").
  setLabelCol("quality")
  //setPredictionCol("prediction")

val paramGrid = new ParamGridBuilder().
  addGrid(lr.elasticNetParam, Array.range(1,6).map(_.toDouble/10) ).
  addGrid(lr.regParam, Array.range(0,6).map(_.toDouble/10) ).
  build()

val cv = new CrossValidator().
  setEstimator(lr).
  setEvaluator(evaluator).
  setEstimatorParamMaps(paramGrid).
  setNumFolds(4) 

val cvModel = cv.fit(training)

cvModel.write.overwrite.save("Model_Parameters")

//Calculate r2 score using evaluetor

val predictions = cvModel.transform(test) 

predictions.write.format("json").mode("overwrite").save("Model_Predictions")
  
val score = evaluator.evaluate(predictions)

println("r2 = " + score)

List(score).toDF.repartition(1).write.format("csv").mode("overwrite").save("Model_R2")