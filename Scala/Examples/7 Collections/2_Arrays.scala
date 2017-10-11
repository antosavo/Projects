/*An Array is an indexed sequence of elements. All the elements in an array are of the same type. 
It is a mutable data structure; you can update an element in an array. It has a fixed length.*/

val a = Array(10, 20, 30, 40)

a(0) = 50

println("a = " + a.toList)

println("a(0) = " + a(0) + "\na(1) = " + a(1))


val b = Array("Hello", " ", "Scala")

println("b = " + b.mkString)


var c = new Array[Int](5)

c(0) = 1
c(1) = 2

println("c = " + c.toList)


var d = Array.range(1,10,2) //1 to 10 with step 2

println("d = " + d.toList)


var e = Array.fill(3)("A")

println("e = " + e.toList)


var f = Array.tabulate(3)(x => Math.cos(x))

println("f = " + f.toList)


import scala.collection.mutable.ArrayBuffer //Creating an Array Whose Size Can Change (ArrayBuffer)

var g = ArrayBuffer[String]()

println("g = " + g.toList)

g += "Ben"
g += "Jerry"
g += "Dale"

println("g = " + g.toList)



