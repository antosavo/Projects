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

val cv = new CrossValidator().
  setEstimator(lr).
  setEvaluator(evaluator).
  setEstimatorParamMaps(paramGrid).
  setNumFolds(4) 

val cvModel = cv.fit(dfv)

cvModel.write.overwrite.save("Model_Parameters_cv")

//Calculate r2 score using evaluetor

val predictions = cvModel.transform(dfv) 

predictions.show()
  
val score = evaluator.evaluate(predictions)

println("r2 = " + score)