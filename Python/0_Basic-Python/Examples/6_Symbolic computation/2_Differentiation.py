import sympy

f = sympy.Symbol("f")
y = sympy.Symbol("y")

f = y**2+y

print "f = y^2+y"
print "df/dy =", f.diff(y)