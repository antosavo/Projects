import breeze.integrate._

def f(x :Double) = math.cos(x)*math.exp(-x)

val It = trapezoid(f, 0, 1, 100) // (begin, end, number of nodes)
println("I_trapezoid = " +It)

val Is = simpson(f, 0, 1, 100)
println("I_simpson = " +Is)