//The "naive" assumptions is: each feature is independent of every other feature 
//C_k = class k
//x = (x_1, x_2, ...x_n) instance with n features
//P(C_k) prior = (number of samples in the class) / (total number of samples)
//P(x_i, C_k) likelihood or feature's distribution
//The assumption for feature's distribution is called the event model of the Naive Bayes classifier.
//y = max[P(C_k)Prod(i=1,n)P(x_i,C_k)] , k E (1,2,3,..)
import org.apache.spark.ml.classification.NaiveBayes
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.linalg.DenseVector
import breeze.plot._

val r = scala.util.Random

val df1 = List.range(0,10).map(i => (0.0, Vectors.dense(r.nextDouble+1,r.nextDouble+1))).toDF("label","features")

val df2 = List.range(0,10).map(i => (1.0, Vectors.dense(r.nextDouble+4,r.nextDouble+4))).toDF("label","features")

val df = df1.unionAll(df2)
df.show()

val model = new NaiveBayes().//setModelType("bernoulli").//Supported options: "multinomial" and "bernoulli". Default is "multinomial"
    fit(df)

val predictions = model.transform(df)
//predictions.printSchema
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
plt.title = "Bayes Classiﬁcation"
plt.xlabel = "x"
plt.xlim(0,6)
plt.ylabel = "y"
plt.ylim(0,6)
fig.saveas("Bayes_Classiﬁcation.png")