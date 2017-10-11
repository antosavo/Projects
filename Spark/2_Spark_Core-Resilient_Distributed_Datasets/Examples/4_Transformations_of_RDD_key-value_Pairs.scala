//keys
//The keys method returns an RDD of only the keys in the source RDD.
val kvRdd = sc.parallelize(List(("a", 1), ("b", 2), ("c", 3)))
val keysRdd = kvRdd.keys
keysRdd.foreach(println)

//values
//The values method returns an RDD of only the values in the source RDD.
val valuesRdd = kvRdd.values
valuesRdd.foreach(println)

//mapValues
//It is similar to the map method, except that it applies
//the input function only to each value in the source RDD, so the keys are not changed.
val valuesDoubled = kvRdd.mapValues(x => 2*x)
valuesDoubled.foreach(println)

//join
//It returns an RDD of pairs, where the first element in a pair is a key found in both source and input RDD
//and the second element is a tuple containing values mapped to that key in the source and input RDD.
val pairRdd1 = sc.parallelize(List(("a", 1), ("b",2), ("c",3)))
val pairRdd2 = sc.parallelize(List(("b", "second"), ("c","third"), ("d","fourth")))
val joinRdd = pairRdd1.join(pairRdd2)
joinRdd.foreach(println)

//leftOuterJoin
val leftOuterJoinRdd = pairRdd1.leftOuterJoin(pairRdd2)
leftOuterJoinRdd.foreach(println)

//rightOuterJoin
val rightOuterJoinRdd = pairRdd1.rightOuterJoin(pairRdd2)
rightOuterJoinRdd.foreach(println)

//fullOuterJoin
//The fullOuterJoin method takes an RDD of key-value pairs as input and performs a full outer join on the
//source and input RDD. It returns an RDD of key-value pairs.
val fullOuterJoinRdd = pairRdd1.fullOuterJoin(pairRdd2)
fullOuterJoinRdd.foreach(println)

//sampleByKey
//The sampleByKey method returns a subset of the source RDD sampled by key. It takes the sampling rate for
//each key as input and returns a sample of the source RDD.
val pairRdd = sc.parallelize(List(("a", 1), ("b",2), ("a", 11),("b",22),("a", 111), ("b",222)))
val sampleRdd = pairRdd.sampleByKey(true, Map("a"-> 1, "b"->0.2))
sampleRdd.foreach(println)

//subtractByKey
//The subtractByKey method takes an RDD of key-value pairs as input and returns an RDD of key-value pairs
//containing only those keys that exist in the source RDD, but not in the input RDD.
val resultRdd = pairRdd1.subtractByKey(pairRdd2)
resultRdd.foreach(println)

//groupByKey
//The groupByKey method returns an RDD of pairs, where the first element in a pair is a key from the source
//RDD and the second element is a collection of all the values that have the same key. 
//The groupByKey method should be avoided. It is an expensive operation since it may shuffle data.
val groupedRdd = pairRdd.groupByKey()
groupedRdd.foreach(println)

//reduceByKey
val pairRdd = sc.parallelize(List(("a", 1), ("b",2), ("c",3), ("a", 11), ("b",22), ("a",111)))
val sumByKeyRdd = pairRdd.reduceByKey((x,y) => x+y)
sumByKeyRdd.foreach(println)
val minByKeyRdd = pairRdd.reduceByKey((x,y) => if (x < y) x else y)
minByKeyRdd.foreach(println)































