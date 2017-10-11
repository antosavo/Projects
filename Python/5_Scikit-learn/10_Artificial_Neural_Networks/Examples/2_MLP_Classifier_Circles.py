import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_circles

x, y = make_circles(n_samples=1000, noise=0.1, factor=0.2)

x_train, x_test, y_train, y_test = train_test_split(x, y)

clf = MLPClassifier(hidden_layer_sizes = (100), solver='lbfgs')
clf.fit(x_train, y_train)

print 'Accuracy:', clf.score(x_test, y_test)

y_pred = clf.predict(x_test)

table = pd.crosstab(np.array(y_test), y_pred, rownames=['Actual'], colnames=['Predictions'])
print table


X1, X2 = np.mgrid[-1.5:1.5:0.01, -1.5:1.5:0.01]

N = X1.shape[0]*X1.shape[1]

X1 = X1.reshape(1,N)
X2 = X2.reshape(1,N)

Z = np.concatenate([X1,X2])

Z = clf.predict(Z.T)

Z = pd.Series(Z).map({0:'pink', 1:'cyan'}) # 0 or 1

plt.scatter(X1, X2, c = Z, marker = ".", edgecolor = "none")
plt.scatter(x[y==0, 0], x[y==0, 1],color='red')
plt.scatter(x[y==1, 0], x[y==1, 1],color='blue')
plt.xlim([-1.5,1.5])
plt.xlabel('x1')
plt.ylim([-1.5,1.5])
plt.ylabel('x2')
plt.savefig('2_Circles.png')
plt.show()