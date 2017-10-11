import sympy

A = sympy.Symbol("A")

A = sympy.Matrix(([3,7],[4,-2]))

b = sympy.Symbol("b")

b = sympy.Matrix((1,2))

#A*x=b => x = (A^-1)*b

print "sol:", A.inv()*b
