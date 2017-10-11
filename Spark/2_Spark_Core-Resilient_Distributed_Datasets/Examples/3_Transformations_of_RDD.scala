//Transformations
/*RDD transformations are conceptually similar to Scala collection methods. 
The key difference is that the Scala collection methods operate on data that 
can fit in the memory of a single machine, whereas RDD
methods can operate on data distributed across a cluster of nodes. 
Another important difference is that RDD
transformations are lazy, whereas Scala collection methods are strict.*/

val lines = sc.textFile("input.txt")
println("Lines:")
lines.foreach(println) //print RDD

//map
val lengths = lines.map(l => l.length)
println("Lengths Lines:")
lengths.foreach(println)  //print RDD

//to array
val A = lengths.collect()
println("A(0)="+A(0))

//to array of dim d
val B = lengths.take(2) //Array from RDD with d=2
println("B(1)="+B(1))

//filter
val longLines = lines.filter(l => l.length > 30)
println("Long Lines:")
longLines.foreach(println)  //print RDD

//flatMap
//It returns a sequence for each input element passed to it. 
val words = lines.flatMap(l => l.split(" "))
println("Words:")
words.foreach(println)  //print RDD

//mapPartitions
val lengths = lines.mapPartitions(iter => iter.map( l => l.length))
println("Lengths Lines:")
lengths.foreach(println)  //print RDD

//union
val linesFile1 = sc.textFile("input1.txt")
val linesFile2 = sc.textFile("input2.txt")
val linesFromBothFiles = linesFile1.union(linesFile2)
println("Union both Files:")
linesFromBothFiles.foreach(println)  //print RDD

//intersection
val mammals = sc.parallelize(List("Lion", "Dolphin", "Whale"))
val aquatics =sc.parallelize(List("Shark", "Dolphin", "Whale"))
val aquaticMammals = mammals.intersection(aquatics)
println("Intersection Linst1 and 2:")
aquaticMammals.foreach(println)  //print RDD

//distinct
val numbers = sc.parallelize(List(1, 2, 3, 4, 3, 2, 1))
val uniqueNumbers = numbers.distinct
println("Distinct numbers in Linst:")
uniqueNumbers.foreach(println)  //print RDD

//cartesian
val numbers = sc.parallelize(List(1, 2, 3, 4))
val alphabets = sc.parallelize(List("a", "b", "c", "d"))
val cartesianProduct = numbers.cartesian(alphabets)
println("Cartesian product Linst 1 and 2:")
cartesianProduct.foreach(println)  //print RDD

//zip
//It returns pairs one element from every RRD
//Both the source RDD and the input RDD must have the same length.
val zippedPairs = numbers.zip(alphabets)
println("Zipped Pairs:")
zippedPairs.foreach(println)  //print RDD

//zipWithIndex
//It gives an index
val alphabetsWithIndex = alphabets.zipWithIndex
println("Alphabets With Index:")
alphabetsWithIndex.foreach(println)  //print RDD

//groupBy
case class Customer(name: String, age: Int, gender: String, zip: String)

val lines = sc.textFile("data.csv")

val customers = lines.map{ l => {
    val a = l.split(",")
    Customer(a(0), a(1).toInt, a(2), a(3))
  }
}
println("Customers:")
customers.foreach(println)  //print RDD

val groupByZip = customers.groupBy( c => c.zip)
println("Customers by zip:")
groupByZip.foreach(println)  //print RDD

//keyBy 
//Similar to groupBy, but the RDD
//returned by keyBy will have the same number of elements as the source RDD.
case class Person(name: String, age: Int, gender: String, zip: String)

val people = lines.map{ l => {
    val a = l.split(",")
    Person(a(0), a(1).toInt, a(2), a(3))
  }
}

val keyedByZip = people.keyBy( p => p.zip)
println("Keyby zip:")
keyedByZip.foreach(println)  //print RDD

//sortBy
val sortedByAge = people.sortBy( p => p.age, false)//( p => p.age, true)
println("Sorted people by age:")
sortedByAge.foreach(println)  //print RDD

//randomSplit
val numbers = sc.parallelize((1 to 10).toList)
val splits = numbers.randomSplit(Array(0.6, 0.2, 0.2))//percentage of splitting
println("Part 0:")
splits(0).foreach(println)
println("Part 1:")
splits(1).foreach(println)
println("Part 2:")
splits(2).foreach(println)

//coalesce
//It takes an integer input and returns a new RDD with the specified number of partitions.
val numbers = sc.parallelize((1 to 10).toList)
val numbersWithOnePartition = numbers.coalesce(1)
println("coalesce:")
numbersWithOnePartition.foreach(println)

//repartition
//The coalesce and repartition methods look similar, but the first one is used for reducing the number
//of partitions in an RDD, while the second one is used to increase the number of partitions in an RDD.
val numbers = sc.parallelize((1 to 10).toList)
val numbersWithFourPartition = numbers.repartition(4)
println("repartition:")
numbersWithFourPartition.foreach(println)

//sample
val numbers = sc.parallelize((1 to 100).toList)
val sampleNumbers = numbers.sample(true, 0.2) //20% sample
println("sample:")
sampleNumbers.foreach(println)






 









