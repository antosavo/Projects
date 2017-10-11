val rawLogs = sc.textFile("data/app.log",1) //1 partition
val logs = rawLogs.map{line => line.trim.toLowerCase()}

//Since the event log data will be queried more than once, let’s cache the logs RDD.
logs.persist() //It essentially materializes an RDD in memory.

val totalCount = logs.count()

val errorLogs = logs.filter{ line =>
	val words = line.split(" ")
	val logLevel = words(1)
	logLevel == "error"
}

//A concise version of the same code is shown here.
val errorLogs = logs.filter{_.split(" ")(1) == " error"}

//If you are not sure whether the columns in a file are separated by a single space, 
//multiple spaces, or tabs, you can use a regex to split the columns.
val errorLogs = logs.filter{_.split("\\s+")(1) == "error"}

val errorCount = errorLogs.count()
val firstError = errorLogs.first()
val first2Errors = errorLogs.take(2)

//longest log line 
val lengths = logs.map{line => line.size}
val maxLen = lengths.reduce{ (a, b) => if (a > b) a else b }

//logs with most words
val wordCounts = logs map {line => line.split("\\s+").size}
val maxWords = wordCounts.reduce{ (a, b) => if (a > b) a else b }

errorLogs.saveAsTextFile("data/error_logs")

//The severity function splits an event log into three words and returns the second word, 
//which is the severity of the log. 
def severity(log: String): String = 
{
	val columns = log.split("\\s+", 3)
	columns(1)
}
//count of logs by severity.
val pairs = logs.map{ log => (severity(log), 1)}
pairs.foreach(println)
val countBySeverityRdd = pairs.reduceByKey{(x,y) => x + y}
val countBySeverity= countBySeverityRdd.collect() //array

//A more concise solution for counting the number of logs by severity is:
val countBySeverityMap = pairs.countByKey()

countBySeverityRdd.saveAsTextFile("data/log-counts-text")
countBySeverityRdd.saveAsSequenceFile("data/log-counts-seq")














