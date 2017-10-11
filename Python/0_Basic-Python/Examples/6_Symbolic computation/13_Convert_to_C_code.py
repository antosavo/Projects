import sympy
from sympy.utilities.codegen import codegen

f = sympy.Function("f")
x = sympy.Symbol("x")

f = sympy.sin(x)

print "f(x) = cos(x)"
print "Series A:", f.series(x, 0, 4)
print "Series B:", f.series(x, 0, 4).removeO()

print codegen(("taylor_sine", f.series(x, 0, 4).removeO() ),"C")[0][1]