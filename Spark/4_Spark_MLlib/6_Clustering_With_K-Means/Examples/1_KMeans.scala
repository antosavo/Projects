//Clustering is an unsupervised learning technique, it is used to find 
//groups of similar observations within a set of unlabeled data.
//K-Means assigns observations to one of K clusters.
//First, the clusters' centroids are initialized to random positions.
//Second, instances are assign to the closest centroids.
//Then we move the centroids to their assigned observations' mean location.
//The optimal values of K-Means' parameters are found by minimizing
//a cost function given by sum of distances from the centers.
import org.apache.spark.ml.clustering.KMeans
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.linalg.DenseVector
import breeze.plot._

val r = scala.util.Random

val df1 = List.range(0,10).map(i => (0.0, Vectors.dense(r.nextDouble+1,r.nextDouble+1))).toDF("label","features")

val df2 = List.range(0,10).map(i => (1.0, Vectors.dense(r.nextDouble+4,r.nextDouble+4))).toDF("label","features")

val df = df1.unionAll(df2)
df.show()

//KMeans
val kmeans = new KMeans().setK(2)

val model = kmeans.fit(df)

//Sum of Squared Errors.
val J = model.computeCost(df)
println("J="+J)

//Shows the result.
println("Cluster Centers: ")
model.clusterCenters.foreach(println)

//Predictions
val predictions = model.transform(df).select(col("features"),col("prediction").cast("double"))
predictions.show()

//Plot

val fig = Figure()
val plt = fig.subplot(0)

val x = predictions.select("features").collect.map(row=>row(0).asInstanceOf[DenseVector](0))

val y = predictions.select("features").collect.map(row=>row(0).asInstanceOf[DenseVector](1))

//val c = predictions.select("prediction").as[Double].collect.map(Map(0.0->"red",1.0->"blue"))

val c = predictions.select("prediction").as[Double].collect.map(Map(0.0 -> java.awt.Color.red, 1.0 -> java.awt.Color.blue))

plt += scatter(x, y, size = x.map(i=>0.1), colors = c)

//plt += plot(x, y, '+', name = "Data", colorcode="red")

plt.legend = true
plt.title = "KMeans"
plt.xlabel = "x"
plt.xlim(0,6)
plt.ylabel = "y"
plt.ylim(0,6)
fig.saveas("KMeans.png")