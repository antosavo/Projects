val myRDD = sc.parallelize(Array(0,12,34,67,55,28,90,99,12,3,56,74,44,87,23,49,89,87,98,100))

myRDD.histogram(4) //4 spaced buckets, between myRDD.min ->  myRDD.max 

myRDD.histogram(Array(0.0, 33.3, 66.6, 100.0)) 