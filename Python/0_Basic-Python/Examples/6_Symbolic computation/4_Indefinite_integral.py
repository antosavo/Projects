import sympy

f = sympy.Symbol("f")
y = sympy.Symbol("y")

f = y**2+y

print "f = y^2+y"
print "Integral f =", f.integrate(y)