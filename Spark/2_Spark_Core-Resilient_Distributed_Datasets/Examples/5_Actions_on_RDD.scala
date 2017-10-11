//Actions
//Actions are RDD methods that return a value to a driver program. 

//collect
//The collect method returns the elements in the source RDD as an array. This method should be used with
//caution since it moves data from all the worker nodes to the driver program. It can crash the driver program
//if called on a very large RDD.
val rdd = sc.parallelize((1 to 10000).toList)
val filteredRdd = rdd.filter( x => (x % 1000) == 0 )
val filterResult = filteredRdd.collect
filterResult.foreach(println)

//count
//The count method returns a count of the elements in the source RDD.
val rdd = sc.parallelize((1 to 10000).toList)
val total = rdd.count
println(total)

//countByValue
//The countByValue method returns a count of each unique element in the source RDD.
//It returns key-value pairs containing each unique element and its count.
val rdd = sc.parallelize(List(1, 2, 3, 4, 1, 2, 3, 1, 2, 1))
val counts = rdd.countByValue
counts.foreach(println)

//first
//The first method returns the first element in the source RDD.
val rdd = sc.parallelize(List(10, 13, 3, 1))
val firstElement = rdd.first
println(firstElement)

//max
//The max method returns the largest element in an RDD.
val maxElement = rdd.max
println(maxElement)

//min
//The min method returns the smallest element in an RDD.
val minElement = rdd.min
println(minElement)

//take
//It returns an array containing the first N element in the source RDD.
val rdd = sc.parallelize(List(2, 5, 3, 1, 50, 100))
val first3 = rdd.take(3)
first3.foreach(println)

//takeOrdered
//The takeOrdered method takes an integer N as input and returns an array containing the N smallest
//elements in the source RDD.
val rdd = sc.parallelize(List(2, 5, 3, 1, 50, 100))
val smallest3 = rdd.takeOrdered(3)
smallest3.foreach(println)

//top
//The top method takes an integer N as input and returns an array containing the N largest elements in the
//source RDD.
val rdd = sc.parallelize(List(2, 5, 3, 1, 50, 100))
val largest3 = rdd.top(3)
largest3.foreach(println)

//fold
//It aggregates the elements in the source RDD using the specified neutral zero
//value and an associative binary operator (0,+), (1,*).
val numbersRdd = sc.parallelize(List(2, 5, 3, 1))
val sum = numbersRdd.fold(0)((partialSum, x) => partialSum + x)
println(sum)
val product = numbersRdd.fold(1)((partialProduct, x) => partialProduct * x)
println(product)

//reduce
//It aggregates the elements of the source RDD using an associative and
//commutative binary operator provided to it. It is similar to the fold method; however, it does not require a
//neutral zero value.
val sum = numbersRdd.reduce((x, y) => x + y)
println(sum)
val product = numbersRdd.reduce((x, y) => x * y)
println(product)









