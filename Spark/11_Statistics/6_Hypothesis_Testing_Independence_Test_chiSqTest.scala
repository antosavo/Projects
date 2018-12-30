import org.apache.spark.mllib.stat.Statistics
import org.apache.spark.mllib.linalg.Matrices

val mat = Matrices.dense(11, 2, Array(24.0, 41.0, 84.0, 107.0, 135.0, 138.0, 126.0, 127.0, 92.0, 49.0, 30.0, 
                                     33.0, 63.0, 81.0, 115.0, 133.0, 145.0, 133.0, 112.0, 83.0, 46.0, 15.0))

//sum((NAi - NBi)^2/(NAi + NBi))
val independenceTestResult = Statistics.chiSqTest(mat)