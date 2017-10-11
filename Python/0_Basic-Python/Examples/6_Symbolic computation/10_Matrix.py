import sympy

A = sympy.Symbol("A")

A = sympy.Matrix(([3,7],[4,2]))

print "A-1:", A.inv()
