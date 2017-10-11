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
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import breeze.plot._

val r = scala.util.Random

val df1 = List.range(0,10).map(i => (0.0, Vectors.dense(r.nextDouble+1,r.nextDouble+1))).toDF("label","features")

val df2 = List.range(0,10).map(i => (1.0, Vectors.dense(r.nextDouble+4,r.nextDouble+4))).toDF("label","features")

val df3 = List.range(0,10).map(i => (2.0, Vectors.dense(r.nextDouble+7,r.nextDouble+7))).toDF("label","features")

val dg = df1.unionAll(df2)
val df = dg.unionAll(df3)
df.show(30)

var x = new Array[Double](9)
var y = new Array[Double](9)

//Elbow Method
for(k <- 2 to 10){

  val kmeans = new KMeans().setK(k)
  val model = kmeans.fit(df)
  val J = model.computeCost(df)

  x(k-2) = k.toDouble
  y(k-2) = J
}

val fig = Figure()
val plt = fig.subplot(0)

plt += plot(x, y, name = "points", colorcode="red")
plt.legend = true
plt.title = "Elbow Method"
plt.xlabel = "k"
//plt.xlim(0,10)
plt.ylabel = "J"
//plt.ylim(0,100)
fig.saveas("Elbow_Method.png")