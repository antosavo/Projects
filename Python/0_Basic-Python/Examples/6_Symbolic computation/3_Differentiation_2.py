import sympy

f = sympy.Symbol("f")
y = sympy.Symbol("y")

f = y**2+y

print "f = y^2+y"
print "d^2f/dy^2 =", f.diff(y,y)