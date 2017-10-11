//countByKey
//The countByKey method counts the occurrences of each unique key in the source RDD. It returns a Map of
//key-count pairs.
val pairRdd = sc.parallelize(List(("a", 1), ("b", 2), ("c", 3), ("a", 11), ("b", 22), ("a", 1)))
val countOfEachKey = pairRdd.countByKey

//lookup
//The lookup method takes a key as input and returns a sequence of all the values mapped to that key in the
//source RDD.
val values = pairRdd.lookup("a")
