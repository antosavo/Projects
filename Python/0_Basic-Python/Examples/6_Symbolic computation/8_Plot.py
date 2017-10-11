import sympy

f = sympy.Function("f")
x = sympy.Symbol("x")

f = sympy.sin(x)

sympy.plot(f,(x,0,6))
