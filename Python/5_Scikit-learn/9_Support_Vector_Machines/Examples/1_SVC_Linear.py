#The SVM main task is basically to discriminate against new observations between two classes.
#Using the perceptron algorithm, we minimized misclassification errors. However, in SVMs,
#our optimization objective is to maximize the margin. The margin is defined as the
#distance between the separating hyperplane (decision boundary) and the training
#samples that are closest to this hyperplane, which are the so-called support vectors.
#The basic idea behind kernel methods is to create nonlinear combinations of the original 
#features to project them onto a higher dimensional space via a mapping function fi() where 
#it becomes linearly separable. We can transform a two-dimensional dataset onto a new 
#three-dimensional feature space where the classes become separable.
#This allows us to separate the two classes via a linear hyperplane
#that becomes a nonlinear decision boundary if we project it back onto the original
#feature space.
#An important parameter is the type of the kernel function, which can be:
#- A linear function
#- A polynomial function
#- A radial basis function
#- A sigmoid function
#A related concept with the SVC algorithm is regularization. It is set by the parameter C: a small value of C
#means that the margin is calculated using many or all of the observations around the line of separation (greater
#regularization), while a large value of C means that the margin is calculated on the observations near to the
#line separation (lower regularization). Unless otherwise specified, the default value of C is equal to 1.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

x = np.array([[1,3],[1,2],[1,1.5],[1.5,2],[2,3],[2.5,1.5],
	    [2,1],[3,1],[3,2],[3.5,1],[3.5,3]])

y = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

model = svm.SVC(kernel='linear', C=1) #Support Vector Classification
model.fit(x,y)

print 'Decision function at [1,1] :', model.decision_function([1,1]) #Distance of the samples X to the separating hyperplane.
print 'Support vectors', model.support_vectors_ #points that participated in the margin calculation.

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
plt.savefig('SVC_linear_C_1_0.png')
plt.show()






