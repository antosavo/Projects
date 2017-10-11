def add1(s1: Int, s2: Int): Int = 
{
	val sum = s1 + s2
	return sum
}

def add2(s1: Int, s2: Int) = s1 + s2

def add3 = (s1: Int, s2: Int) => s1 + s2

val x = 1
val y = 2

println("add1 = " + add1(x,y))
println("add2 = " + add2(x,y))
println("add3 = " + add3(x,y))
