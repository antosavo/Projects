import org.apache.spark.ml.clustering.KMeans
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.linalg.DenseVector
import org.apache.spark.ml.feature.{VectorAssembler,StringIndexer}
import org.apache.spark.ml.Pipeline
import breeze.plot._

//DataFrame

val df = spark.read.
  format("csv").
  option("header", "true").
  option("inferschema", "true").
  option("delimiter",",").
  load("Iris.csv")

df.printSchema

df.show()

println("\nColumn Names:")//df.columns is an array
df.columns.foreach(println)

println("\nNumber Columns:" + df.columns.length)

println("\nNumber Rows:" + df.count)

println("\nDistinct species:")
df.select("species").distinct.collect.foreach(println)

println("\nFrequency species:")
df.groupBy("species").count.select(col("species"),(col("count")/df.count).as("frequency")).show()

//Vectorize features
val features = df.columns.slice(0, df.columns.length -1)

println("features:" + features)

val assembler = new VectorAssembler().
  setInputCols(features).//setInputCols(Array("_c1", "_c2")).
  setOutputCol("features")

//String Indexer
val indexer = new StringIndexer().
  setInputCol("species").
  setOutputCol("label")

//Pipeline
val pipeline = new Pipeline().
  setStages(Array(assembler, indexer))

val dfi = pipeline.fit(df).transform(df).select("features","label")
dfi.show()

//KMeans
val kmeans = new KMeans().setK(3)

val model = kmeans.fit(dfi)

//Sum of Squared Errors.
val J = model.computeCost(dfi)
println("J="+J)

//Shows the result.
println("Cluster Centers: ")
model.clusterCenters.foreach(println)

//Predictions
val predictions = model.transform(dfi).select(col("features"),col("prediction").cast("double"))
predictions.show()

//Plot

val fig = Figure()
val plt = fig.subplot(0)

val x = predictions.select("features").collect.map(row=>row(0).asInstanceOf[DenseVector](0))

val y = predictions.select("features").collect.map(row=>row(0).asInstanceOf[DenseVector](1))

//val c = predictions.select("prediction").as[Double].collect.map(Map(0.0->"red",1.0->"blue"))

val c = predictions.select("prediction").as[Double].collect.map(Map(0.0 -> java.awt.Color.red, 1.0 -> java.awt.Color.blue,  2.0 -> java.awt.Color.green))

plt += scatter(x, y, size = x.map(i=>0.1), colors = c)

//plt += plot(x, y, '+', name = "Data", colorcode="red")

plt.legend = true
plt.title = "KMeans"
plt.xlabel = "x"
//plt.xlim(0,6)
plt.ylabel = "y"
//plt.ylim(0,6)
fig.saveas("KMeans_Iris.png")
