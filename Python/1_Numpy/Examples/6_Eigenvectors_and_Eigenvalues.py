import numpy as np
import  numpy.linalg as la

A = np.random.rand(2,2)

#A = np.eye(2) #A = I

print "A = ", A

e , v = la.eig(A) #A*v = e*v

print " Eigenvalues = ", e
print " e[0] = ", e[0]
print " e[1] = ", e[1]
print " Eigenvectors = ", v
print " v[0] = ", v[:,0]
print " v[1] = ", v[:,1]
print " A*v[0]/e[0] = ",  np.dot(A,v[:,0])/e[0]
print " A*v[1]/e[1] = ",  np.dot(A,v[:,1])/e[1]