import sympy
#from sympy import sin

f = sympy.Function("f")
x = sympy.Symbol("x")

f = sympy.sin(x)

print "f(x) = cos(x)"
print "Series A:", f.series(x, 0, 4)
print "Series B:", f.series(x, 0, 4).removeO()
