//Logistic regression can be used for binary classification, a task in which an
//instance must be assigned to one of two classes.
//LR uses a logistic function to relate a linear combination of the explanatory
//variables to a value between zero and one which corresponds to the chance to belong to one of the two classes.
//The predicted probability can then simply be converted into a binary outcome via a step function.
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.linalg.DenseVector
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import breeze.plot._

val r = scala.util.Random

val df1 = List.range(0,10).map(i => (0.0, Vectors.dense(r.nextDouble+1,r.nextDouble+1))).toDF("label","features")

val df2 = List.range(0,10).map(i => (1.0, Vectors.dense(r.nextDouble+4,r.nextDouble+4))).toDF("label","features")

val df = df1.unionAll(df2)
df.show()

val lr = new LogisticRegression().
  setMaxIter(20)
  //setRegParam(0.3).//Default is 0.0.
  //setElasticNetParam(0.8)//Default is 0.0 which is an L2 penalty.

val model = lr.fit(df)

println("Coefficients:" + model.coefficients)
println("Intercept:" + model.intercept)

val predictions = model.transform(df)
//predictions.printSchema
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
plt.title = "Logistic Regression"
plt.xlabel = "x"
plt.xlim(0,6)
plt.ylabel = "y"
plt.ylim(0,6)
fig.saveas("Logistic_Regression.png")