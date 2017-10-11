#The Principal Component Analysis (PCA) is commonly
#used to explore and visualize high-dimensional data sets. It can also be used to
#compress data, and process data before it is used by another estimator. PCA reduces
#a set of possibly-correlated, high-dimensional variables to a lower-dimensional
#set of linearly uncorrelated variables called principal components.
#PCA can project data in a high-dimensional space
#to a lower-dimensional space that retains as much of the variance as possible. PCA
#rotates the data set to align with its principal components to maximize the variance
#contained within the first several principal components.
#The principal components of a matrix are the eigenvectors of its covariance matrix, ordered by
#their corresponding eigenvalues. The eigenvector with the greatest eigenvalue is the
#first principal component; the second principal component is the eigenvector with
#the second greatest eigenvalue, and so on.
#PCA requires normalized eigenvectors.
import numpy as np
import pandas as pd
import numpy.linalg as la
from sklearn.decomposition import PCA


data = {'x1' : [0.9,2.4,1.2,0.5,0.3,1.8,0.5,0.3,2.5,1.3],
	'x2' : [1,2.6,1.7,0.7,0.7,1.4,0.6,0.6,2.6,1.1]}

X = pd.DataFrame(data)

#Using sklearn
pca = PCA(n_components=1)
reduced_X = pca.fit_transform(X)
print 'Principal component using sklearn:\n', reduced_X

print '\nStep by step:\n'
#1) The first step of PCA is to subtract the mean of each explanatory variable from each observation.
X = (X - X.mean())
print '1) X - <X>=\n', X

#2) Next, we must calculate the principal components of the data. Recall that the
#principal components are the eigenvectors of the data's covariance matrix ordered
#by their eigenvalues.
C = X.cov() #The covariance is normalized by N-1 
print '\n2) Covariance(x1,x2)=\n', C

e , v = la.eig(C) #C*v = e*v

print " Eigenvalues e = ", e
#print " e[0] = ", e[0]
#print " e[1] = ", e[1]
print " Eigenvectors v =\n", v
#print " v[0] = ", v[:,0]
#print " v[1] = ", v[:,1]
#print " C*v[0]/e[0] = ",  np.dot(C,v[:,0])/e[0]
#print " C*v[1]/e[1] = ",  np.dot(C,v[:,1])/e[1]

#3) Next, we will project the data onto the principal components. The first eigenvector
#has the greatest eigenvalue and is the first principal component. We will build a
#transformation matrix in which each column of the matrix is the eigenvector for
#a principal component.
print '\n3) Principal component X*v[0] :\n', np.dot(X,v[:,0])



