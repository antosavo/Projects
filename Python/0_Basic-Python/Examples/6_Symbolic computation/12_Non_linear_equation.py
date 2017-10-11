import sympy

x = sympy.Symbol("x")

eq = sympy.Eq(x-x**3, 0)

print "eq : x - x**3 = 0"
print "sol:", sympy.solve(eq,x)