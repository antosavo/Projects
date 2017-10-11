import numpy as np

A = np.array([[1,2,3],[4,5,6]])

print "A = ", A

print "A shape = ", A.shape

print "A[0,1] = ", A[0,1]

print "A[0,1] = ", A[0][1]

print "First column A = ", A[:,0]

print "Second column A = ", A[:,1]

print "First row A = ", A[0,:]

print "Second row A = ", A[1,:]

B = np.zeros((5,4))

print "B = ", B

I = np.eye(3) # Matrix I

print "I = ", I
