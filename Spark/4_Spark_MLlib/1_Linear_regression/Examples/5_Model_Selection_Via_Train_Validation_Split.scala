import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.tuning.{TrainValidationSplit, ParamGridBuilder}
import breeze.plot._

//DataFrame

val df = spark.read.
  format("csv").
  option("header", "true").
  option("inferschema", "true").
  option("delimiter",";").
  load("winequality-red.csv")

df.printSchema

//Vectorize features

val features = df.columns.slice(0, df.columns.length -1)

println("features:" + features)

val assembler = new VectorAssembler().
  setInputCols(features).//setInputCols(Array("_c1", "_c2")).
  setOutputCol("features")

val dfv = assembler.transform(df).select(col("quality").cast("Double"), col("features"))

dfv.show()

//Cros validation

val lr = new LinearRegression().
  setMaxIter(100).//setElasticNetParam(1.0).
  setLabelCol("quality").//by default input columns: label and features
  setFeaturesCol("features")

val evaluator = new RegressionEvaluator().setMetricName("r2").
  setLabelCol("quality").
  setPredictionCol("prediction")

val paramGrid = new ParamGridBuilder().
  addGrid(lr.elasticNetParam, Array(0.1, 0.5, 1.0)).
  build()

val tv = new TrainValidationSplit().
  setEstimator(lr).
  setEvaluator(evaluator).
  setEstimatorParamMaps(paramGrid).
  setTrainRatio(0.8)
  // 80% of the data will be used for training and the remaining 20% for validation.

val tvModel = tv.fit(dfv)

tvModel.write.overwrite.save("Model_Parameters_tv")

//Calculate r2 score using evaluetor

val predictions = tvModel.transform(dfv) 

predictions.show()
  
val score = evaluator.evaluate(predictions)

println("r2 = " + score)