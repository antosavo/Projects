import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.linalg.Vectors

//Read File

val data = sc.textFile("data_1.txt")

val df = data.
  map{row => row.split(" ")}.
  map{col => (col(0).toDouble, Vectors.dense(col(1).toDouble, col(2).toDouble) )}.
  toDF("label", "features")

df.show()

//Fit

val lr = new LinearRegression().
  setMaxIter(100).
  setElasticNetParam(1.0)

val model = lr.fit(df)

println("Coefficients:" + model.coefficients)

println("Intercept:" + model.intercept)

println("r2:" + model.summary.r2)

println("NumIterations:" + model.summary.totalIterations)

println("Predictions:")
model.transform(df).show()

