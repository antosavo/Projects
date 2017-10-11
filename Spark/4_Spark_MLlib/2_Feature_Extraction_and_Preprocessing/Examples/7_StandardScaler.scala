import org.apache.spark.ml.feature.StandardScaler
import org.apache.spark.ml.linalg.Vectors

val dataFrame = List(
  (0.0, Vectors.dense(0.0, 1)),
  (1.0, Vectors.dense(1.9, 4)),
  (2.0, Vectors.dense(4.1, 8)),
  (3.0, Vectors.dense(5.9, 12)),
  (4.0, Vectors.dense(8.1, 16)),
  (5.0, Vectors.dense(9.9, 20))).toDF("label", "features")

val scaler = new StandardScaler().
  setInputCol("features").
  setOutputCol("scaledFeatures").
  setWithMean(true)
  //setWithStd(true)//false

val scalerModel = scaler.fit(dataFrame)

// Normalize each feature to have unit standard deviation.
val scaledData = scalerModel.transform(dataFrame)

scaledData.show()