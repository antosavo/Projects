#Let's see SVC using a polynomial kernel.
#The degree of the polynomial can be defined by the degree option. 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

x = np.array([[1,3],[1,2],[1,1.5],[1.5,2],[2,3],[2.5,1.5],
	    [2,1],[3,1],[3,2],[3.5,1],[3.5,3]])

y = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

model = svm.SVC(kernel='poly', C=1, degree=3) #Support Vector Classification
model.fit(x,y)

X1, X2 = np.mgrid[0:4:0.01, 0:4:0.01]

N = X1.shape[0]*X1.shape[1]

X1 = X1.reshape(1,N)
X2 = X2.reshape(1,N)

Z = np.concatenate([X1,X2])

Z = model.predict(Z.T) # 0 or 1

plt.scatter(X1, X2, c = Z, cmap = "cool", marker = ".", edgecolor = "none")
plt.scatter(x[:,0], x[:,1], c=y, s=60)
plt.scatter(model.support_vectors_[:,0], model.support_vectors_[:,1],s=200,facecolors='none')
plt.xlim([0,4])
plt.xlabel('x1')
plt.ylim([0,4])
plt.ylabel('x2')
plt.savefig('SVC_poly.png')
plt.show()






