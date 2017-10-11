import org.apache.spark.ml.regression.LinearRegression

//Read File

val df = spark.read.format("libsvm").
  load("data_2.txt")

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