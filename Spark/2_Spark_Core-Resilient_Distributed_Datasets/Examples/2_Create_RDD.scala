//parallelize
val xs = (1 to 100).toList
val rdd1 = sc.parallelize(xs)

//textFile
val rdd2 = sc.textFile("input.txt",1)//with 1 partition

//wholeTextFiles
val rdd3 = sc.wholeTextFiles("*.txt")//This method reads all text files in a directory
// and returns an RDD of key-value pairs. 

//sequenceFile
val rdd4 = sc.sequenceFile[String, String]("input.txt")
//The sequenceFile method reads key-value pairs from a sequence file