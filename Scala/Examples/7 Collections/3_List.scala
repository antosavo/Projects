/*A List is a linear sequence of elements of the same type. 
It cannot be modified after it has been created.*/

val xs = List(10,20,30,40)

println("xs = " +xs)

println("xs(0) = " + xs(0) + "\nxs(1) = " + xs(1))


val ys = (1 to 10).toList

println("ys = " +ys)


val a = Array(10, 20, 30, 40)

println("a = " +a.toList)
