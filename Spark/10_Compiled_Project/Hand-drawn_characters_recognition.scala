import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.linalg.DenseVector
import org.apache.spark.ml.feature.PCA
import org.apache.spark.ml.feature.StandardScaler
import org.apache.spark.ml.tuning.{CrossValidator, ParamGridBuilder}
import org.apache.spark.ml.classification.{LogisticRegression,OneVsRest}
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import Image.Processing._


object PCAHR
{

def main(args: Array[String]) 
{

val spark = SparkSession.
  builder.
  appName("MyApp").
  getOrCreate()
  //config("spark.sql.caseSensitive", "true").
import spark.implicits._

//Load images and transform them into feature vectors

var data = Vector.empty[(Double, org.apache.spark.ml.linalg.Vector)]

var path = ""

for(j <- 1 to 10)
{
  for(k <- 1 to 10)
    {

    val J = j.toString
    val K = k.toString

    if( j <= 9 & k <= 9 ){
    path = "../Datasets/Hand_drawn_characters/Sample00" + J + "/img00" + J + "-00" + K + ".png"
    } else if( j <= 9 & k > 9 ){
    path = "../Datasets/Hand_drawn_characters/Sample00" + J + "/img00" + J + "-0" + K + ".png"
    } else if( j > 9 & k <= 9 ){
    path = "../Datasets/Hand_drawn_characters/Sample0" + J + "/img0" + J + "-00" + K + ".png"
    } else{
    path = "../Datasets/Hand_drawn_characters/Sample0" + J + "/img0" + J + "-0" + K + ".png"
    }
        
    val image = readImage(path)

    val acimage = autoCropImage(image)

    val rimage = resizeImage(acimage, 10, 15)

    val m = covertToArray(rimage).max

    val V = Vectors.dense(covertToArray(rimage).map(x => x - m)) //5400 d densevector

    data = data :+ (j.toDouble,V)

    }
}

//Create Dataframe

val df = data.toDF("label","features")

//Split into train and test sets

val Array(trainingData, testData) = df.randomSplit(Array(0.7, 0.3))

//Scale the features

val scaler = new StandardScaler().
  setInputCol("features").
  setOutputCol("scaledFeatures")

val s = scaler.fit(trainingData)

val trainingData_s = s.transform(trainingData)
val testData_s = s.transform(testData)

//Dimensionality Reduction with PCA

val pca = new PCA().
    setInputCol("scaledFeatures").
    setOutputCol("pcaFeatures").
    setK(30)

val p = pca.fit(trainingData_s)

val trainingData_p = p.transform(trainingData_s)
val testData_p = p.transform(testData_s)

//Hyperparameter optimization with cross-validation

/*
val lr = new LogisticRegression().
    setFeaturesCol("pcaFeatures").
    setMaxIter(100)

val ovr = new OneVsRest().
    setClassifier(lr)

val evaluator = new MulticlassClassificationEvaluator().setMetricName("accuracy")

val paramGrid = new ParamGridBuilder().
  addGrid(lr.regParam, Array(0.01, 0.1, 1, 10, 100)).
  addGrid(lr.elasticNetParam, Array(0.2,0.4,0.6,0.8,1.0)).
  build()

val CV = new CrossValidator().
  setEstimator(ovr).
  setEvaluator(evaluator).
  setEstimatorParamMaps(paramGrid).
  setNumFolds(5)

val model = CV.fit(trainingData_p)

model.write.overwrite.save("Model_Parameters")
*/

//Train the model

val lr = new LogisticRegression().
    setFeaturesCol("pcaFeatures").
    setMaxIter(100)

val ovr = new OneVsRest().
    setClassifier(lr)

val model = ovr.fit(trainingData_p)

//Make predictions

val predictions = model.transform(testData_p)

//Evaluate the model

val evaluator = new MulticlassClassificationEvaluator().
    setLabelCol("label").
    setPredictionCol("prediction").
    setMetricName("accuracy")
    
val accuracy = evaluator.evaluate(predictions)
println("Accuracy: " + accuracy)

//Crosstabulation

println("Crosstabulation:")
predictions.stat.crosstab("label", "prediction").sort("label_prediction").show()

spark.stop()

}

}