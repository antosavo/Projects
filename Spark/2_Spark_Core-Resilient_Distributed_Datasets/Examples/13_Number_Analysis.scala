val xs = (1 to 1000).toList
val xsRdd = sc.parallelize(xs)

val evenRdd = xsRdd.filter{ _ % 2 == 0}
val count = evenRdd.count
val first = evenRdd.first
val first5 = evenRdd.take(5)