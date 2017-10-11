val L = List(1, 2, 3, 4, 5)

println("L = " +L)


val M = L.map(i => i*10.0)

println("M = " +M)


val N = L map(_*10.0) //The underscore character represents every element of L

println("N = " +N)

