import sympy

f = sympy.Function("f")
x = sympy.Symbol("x")

eq = sympy.Eq(f(x).diff(x,x)+5.0*f(x), 0)

print "eq : f''(x) + 5*f(x) = 0"
print "A:", sympy.dsolve(eq,f(x))
print "B:", sympy.dsolve(f(x).diff(x,x)+5.0*f(x),f(x))