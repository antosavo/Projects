import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.linalg.DenseVector
import breeze.plot._

//DataFrame

val df = List(
  (0.0, Vectors.dense(0.0)),
  (1.0, Vectors.dense(1.9)),
  (2.0, Vectors.dense(4.1)),
  (3.0, Vectors.dense(5.9)),
  (4.0, Vectors.dense(8.1)),
  (5.0, Vectors.dense(9.9))).toDF("label", "features")

df.show()

//Explain Linear Regression:
println("Explain Linear Regression:\n")
println((new LinearRegression().explainParams)+"\n")

//Fit

val lr = new LinearRegression().
  setMaxIter(100).
  setElasticNetParam(1.0)
  //setLabelCol("label").//by default input columns: label and features
  //setFeaturesCol("features")
  //setSolver() this can be "l-bfgs", "normal" and "auto". 
  //"l-bfgs" denotes Limited-memory BFGS which is a limited-memory quasi-Newton optimization method. 
  //"normal" denotes using Normal Equation as an analytical solution to the linear regression problem. 
  //The default value is "auto" which means that the solver algorithm is selected automatically.

val model = lr.fit(df)

println("Coefficients:" + model.coefficients)

println("Intercept:" + model.intercept)

println("r2:" + model.summary.r2)

println("NumIterations:" + model.summary.totalIterations)

val dfp = model.transform(df)

println("Predictions:")
dfp.show()

//Plot

val fig = Figure()
val plt = fig.subplot(0)

//val y = df.select("label").collect.map(i=>i(0).toString.toDouble)
//val y = df.select("label").collect.map(i=>i(0).asInstanceOf[Double])
//val x = dfp.select("features").collect.map(i=>i(0).toString.substring(1,i(0).toString.length-1).toDouble)

val x = dfp.select("features").collect.map(row=>row(0).asInstanceOf[DenseVector](0))

val y = dfp.select("label").as[Double].collect

val yp = dfp.select("prediction").as[Double].collect

plt += plot(x, y, '+', name = "Data", colorcode="red")
plt += plot(x, yp, '-', name = "Fit", colorcode="blue")

plt.legend = true
plt.title = "Linear Regression"
plt.xlabel = "x"
plt.xlim(0,11)
plt.ylabel = "y"
plt.ylim(0,6)
fig.saveas("Linear_Regression.png")
