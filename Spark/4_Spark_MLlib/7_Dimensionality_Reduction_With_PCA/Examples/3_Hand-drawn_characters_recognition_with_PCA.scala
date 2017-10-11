import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.linalg.DenseVector
import org.apache.spark.ml.feature.{VectorAssembler,StringIndexer,IndexToString}
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.feature.PCA
import Image.Processing._
import org.apache.spark.ml.classification.{LogisticRegression, OneVsRest}
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator

var data = Vector.empty[(Double, org.apache.spark.ml.linalg.Vector)]

var path = ""

for(j <- 1 to 10)
{
  for(k <- 1 to 20)
    {

    val J = j.toString
    val K = k.toString

    if( j <= 9 & k <= 9 ){
    path = "Hand-drawn_characters/Sample00" + J + "/img00" + J + "-00" + K + ".png"
    } else if( j <= 9 & k > 9 ){
    path = "Hand-drawn_characters/Sample00" + J + "/img00" + J + "-0" + K + ".png"
    } else if( j > 9 & k <= 9 ){
    path = "Hand-drawn_characters/Sample0" + J + "/img0" + J + "-00" + K + ".png"
    } else{
    path = "Hand-drawn_characters/Sample0" + J + "/img0" + J + "-0" + K + ".png"
    }

    val image = readImage(path)

    val acimage = autoCropImage(image)

    val rimage = resizeImage(acimage, 10, 15)

    val m = covertToArray(rimage).max

    val V = Vectors.dense(covertToArray(rimage).map(x => x - m)) //5400 d densevector

    data = data :+ (j.toDouble,V)

    }
}

val dfi = data.toDF("label","allFeatures")

dfi.show(200)

//PCA
val pca = new PCA().
    setInputCol("allFeatures").
    setOutputCol("features").
    setK(20).
    fit(dfi)

val df = pca.transform(dfi).select("label","features")

//Split training, test data
val Array(trainingData, testData) = df.randomSplit(Array(0.7, 0.3))

//Train a Logistic Regression model
val lr = new LogisticRegression().setMaxIter(50)

//One Vs Rest Classifier.
val ovr = new OneVsRest().setClassifier(lr)
val model = ovr.fit(trainingData)

//Select example rows to display
val predictions = model.transform(testData)
predictions.show()

//Evaluator
val evaluator = new MulticlassClassificationEvaluator().
    setLabelCol("label").
    setPredictionCol("prediction").
    setMetricName("accuracy")
    
val accuracy = evaluator.evaluate(predictions)
println("Accuracy: " + accuracy)

//Crosstabulation
println("Crosstabulation:")
predictions.stat.crosstab("label", "prediction").show()
