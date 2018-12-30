import org.apache.spark.mllib.stat.Statistics
import org.apache.spark.mllib.linalg.Vectors

val observed = Vectors.dense(0.1, 0.15, 0.2, 0.3, 0.25)
val expected = Vectors.dense(0.1, 0.15, 0.2, 0.3, 0.25)

// Chi_2 = sum((Oi - Ei)^2/Ei)
val goodnessOfFitTestResult = Statistics.chiSqTest(observed,expected)

// summary of the test including the p-value, degrees of freedom, test statistic, the method
// used, and the null hypothesis.