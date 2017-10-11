import sympy
from sympy import oo

f = sympy.Function("f")
x = sympy.Symbol("x")

f = sympy.exp(-x)

print "Limit:",sympy.limit(f,x,oo)
