import org.apache.spark.ml.classification.{LogisticRegression, OneVsRest}
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator

val r = scala.util.Random

val df1 = List.range(0,10).map(i => (0.0, Vectors.dense(r.nextDouble+1,r.nextDouble+1))).toDF("label","features")

val df2 = List.range(0,10).map(i => (1.0, Vectors.dense(r.nextDouble+4,r.nextDouble+4))).toDF("label","features")

val df3 = List.range(0,10).map(i => (2.0, Vectors.dense(r.nextDouble+6,r.nextDouble+6))).toDF("label","features")

val df_12 = df1.unionAll(df2)
val df = df_12.unionAll(df3)
df.show(30)

val lr = new LogisticRegression().
  setMaxIter(20)
  //setRegParam(0.3).//Default is 0.0.
  //setElasticNetParam(0.8)//Default is 0.0 which is an L2 penalty.

//One Vs Rest Classifier.
val ovr = new OneVsRest().setClassifier(lr)
val model = ovr.fit(df)

//Predictions
val predictions = model.transform(df)
predictions.show(30)

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