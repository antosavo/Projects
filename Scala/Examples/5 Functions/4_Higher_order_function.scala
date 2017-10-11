def apply_f(f: Double => Double, v: Double) = f(v)

var x = 1.0

var y = apply_f(Math.cos,x)

println("y="+y)