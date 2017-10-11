import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.linalg.Vectors

//Read File

val df = spark.read.
    format("csv").
    option("inferschema", "true").
    option("delimiter"," ").
    load("data_1.txt")

df.show()

//Transform features to dense vector

val features = udf((x: Double, y:Double) => Vectors.dense(x,y))

val training_df = df.select(col("_c0").cast("Double").as("label"),features(col("_c1"),col("_c2")).as("features"))

training_df.show()

//Fit

val lr = new LinearRegression().
  setMaxIter(100).
  setElasticNetParam(1.0)

val model = lr.fit(training_df)

println("Coefficients:" + model.coefficients)

println("Intercept:" + model.intercept)

println("r2:" + model.summary.r2)

println("NumIterations:" + model.summary.totalIterations)

println("Predictions:")
model.transform(training_df).show()
