import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._

object WordCount {
 def main(args: Array[String])
 {
  val sc = new SparkContext()
  val lines = sc.textFile("input.txt")

  val wordCounts = lines.flatMap{line => line.split(" ")}.
                         map(word => (word, 1)).
                         reduceByKey(_ + _)

  wordCounts.saveAsTextFile("output")

  println("OK")

}
}
