def F(n: Int, f: (Double) => Double) = 
{
	val x = n * 10.0
	f(x)
}

def g(x: Double) = Math.cos(x) + Math.sin(x)

val n = 2

println("F(n,g) = " + F(n,g))

