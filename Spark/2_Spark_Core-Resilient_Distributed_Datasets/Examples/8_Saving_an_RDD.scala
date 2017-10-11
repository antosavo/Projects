//saveAsTextFile
val numbersRdd = sc.parallelize((1 to 10000).toList)
val filteredRdd = numbersRdd.filter( x => x % 1000 == 0)
filteredRdd.saveAsTextFile("numbers-as-text")

//saveAsObjectFile
//The saveAsObjectFile method saves the elements of the source RDD as serialized Java objects in the
//specified directory.
filteredRdd.saveAsObjectFile("numbers-as-object")

//saveAsSequenceFile
val pairs = (1 to 10000).toList.map(x => (x, x*2))
val pairsRdd = sc.parallelize(pairs)
//val filteredPairsRdd = pairsRdd.filter( _._1 % 1000 ==0 )
val filteredPairsRdd = pairsRdd.filter{ case (x, y) => x % 1000 ==0 }
filteredPairsRdd.saveAsSequenceFile("pairs-as-sequence")
filteredPairsRdd.saveAsTextFile("pairs-as-text")
