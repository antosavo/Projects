val lines = sc.textFile("input.txt")
val plines = lines.filter( l => l.contains("people"))
//The textFile method does not actually read
//a file right when you call it. Similarly, 
//the filter method does not immediately iterate through all the
//elements in the source RDD.
plines.foreach(println) //now they do things
//RDD transformations are computed when an application 
//calls an action method of an RDD or saves an RDD to a storage system.
val nplines = plines.count
plines.cache()//The cache method stores an RDD in the memory of the executors across a cluster.

