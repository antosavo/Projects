import numpy as np
import  numpy.linalg as la

A = np.random.rand(2,2)
b = np.random.rand(2)

print "A = ", A
print "A^T = ", np.transpose(A)
print "A^-1 = ", la.inv(A)
print "b = ", b


x = la.solve(A,b) #solve the system of equatioms Ax = b

print "x1 = (A^-1)b = ", x

A_1 = la.inv(A)

print "x2 = (A^-1)b = ", np.dot(A_1,b)


