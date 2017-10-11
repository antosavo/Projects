import org.apache.spark.ml.feature.PolynomialExpansion
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.regression.LinearRegression
import breeze.plot._

//DataFrame

val df = List(
  (0.1, Vectors.dense(0.0)),
  (0.9, Vectors.dense(1.0)),
  (8.1, Vectors.dense(2.0)),
  (26.9, Vectors.dense(3.0)),
  (64.1, Vectors.dense(4.0)),
  (124.9, Vectors.dense(5.0))).toDF("label", "features")

df.show()

//Polynomial Expansion

val polynomialExpansion = new PolynomialExpansion().
  setInputCol("features").
  setOutputCol("polyFeatures").
  setDegree(3)

val dfp = polynomialExpansion.transform(df)

dfp.show()

//Fit

val lr = new LinearRegression().
  setMaxIter(100).
  setElasticNetParam(1.0).
  setLabelCol("label").
  setFeaturesCol("polyFeatures")

val model = lr.fit(dfp)

println("Coefficients:" + model.coefficients)

println("Intercept:" + model.intercept)

println("r2:" + model.summary.r2)

println("NumIterations:" + model.summary.totalIterations)

val df_pred = model.transform(dfp) 

println("Predictions:")
df_pred.show()

//Plot
val fig = Figure()
val plt = fig.subplot(0)


val x = Array.range(0,6).map(x => x.toDouble)

val y = df_pred.select("label").as[Double].collect

val y_pred = df_pred.select("prediction").as[Double].collect

plt += plot(x, y, '+', name = "Data", colorcode="red")
plt += plot(x, y_pred, '-', name = "Fit", colorcode="blue")

plt.legend = true
plt.title = "Polynomial Regression"
plt.xlabel = "x"
//plt.xlim(0,11)
plt.ylabel = "y"
//plt.ylim(0,6)
fig.saveas("Polynomial_Regression.png")