import numpy as np
import numpy.random

A = np.random.rand(2,2) #generates a random(0,1) 2 by 2 matrix

print "A = ", A

x = np.random.rand(2) #generates a random(0,1) 2-element vector

print "x = ", x

y = np.dot(A,x) #multiply matrix A with vector x

print "y = Ax = ", y
