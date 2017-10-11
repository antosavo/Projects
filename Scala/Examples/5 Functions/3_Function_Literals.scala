def F(n: Int, f: (Double) => Double) = 
{
	val x = n * 10.0
	f(x)
}

val n = 2

println("F = " + F(n, (x: Double) => x + 2.0 ) )

