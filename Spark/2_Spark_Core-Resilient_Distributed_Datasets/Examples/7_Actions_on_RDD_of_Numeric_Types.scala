//mean
//The mean method returns the average of the elements in the source RDD.
val numbersRdd = sc.parallelize(List(2, 5, 3, 1))
val mean = numbersRdd.mean

//stdev
//The stdev method returns the standard deviation of the elements in the source RDD.
val stdev = numbersRdd.stdev

//sum
//The sum method returns the sum of the elements in the source RDD.)
val sum = numbersRdd.sum

//variance
//The variance method returns the variance of the elements in the source RDD.
val variance = numbersRdd.variance
