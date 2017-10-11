import org.apache.spark.ml.feature.PCA
import org.apache.spark.ml.linalg.Vectors

val df = List(
    (0.0, Vectors.dense(0.0,2.0,0.0)),
    (1.0, Vectors.dense(1.9,3.0,4.0)),
    (2.0, Vectors.dense(4.1,5.0,4.0)),
    (3.0, Vectors.dense(5.9,0.0,0.0)),
    (4.0, Vectors.dense(8.1,6.0,7.0)),
    (5.0, Vectors.dense(9.9,9.0,5.0))).toDF("label", "features")

df.show()

val pca = new PCA().
    setInputCol("features").
    setOutputCol("pcaFeatures").
    setK(2).
    fit(df)

val pcaDF = pca.transform(df)
val result = pcaDF.select("pcaFeatures")

result.show()