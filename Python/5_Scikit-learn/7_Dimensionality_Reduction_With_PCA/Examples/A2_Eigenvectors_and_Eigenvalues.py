import numpy as np
import  numpy.linalg as la

#A = np.random.rand(2,2)
#A = np.eye(2) #A = I
A = np.array([[1, -2], [2, -3]])


print "A = ", A

e, v = la.eig(A) #A*v = e*v

print " Eigenvalues = ", e

print " Eigenvectors = ", v