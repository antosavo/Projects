import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale

data = pd.read_csv('Iris.csv')

print 'Some Data:\n', data.head()
print 'Unique Species:', data['species'].unique()

colnames = data.columns.values
print 'Column Names:', colnames

x = scale(data[colnames[0:2]])
y = data[colnames[4]]

model = KMeans(n_clusters=3, init ='k-means++')
model.fit(x)

colors = y.map({'setosa':'red', 'versicolor':'blue', 'virginica':'green'})

max1 = x[:,0].max() +1
max2 = x[:,1].max() +1

min1 = x[:,0].min() -1
min2 = x[:,1].min() -1

X1, X2 = np.mgrid[min1:max1:0.01, min2:max2:0.01]

N = X1.shape[0]*X1.shape[1]

X1 = X1.reshape(1,N)
X2 = X2.reshape(1,N)

Z = np.concatenate([X1,X2])

Z = model.predict(Z.T)

Z = pd.Series(Z).map({0:'pink', 1:'yellow', 2:'cyan'}) # 0 or 1

plt.scatter(X1, X2, c = Z, marker = ".", edgecolor = "none")
plt.scatter(x[:,0], x[:,1], c = colors, s=60)
plt.xlim([min1,max1])
plt.xlabel('sepal_length')
plt.ylim([min2,max2])
plt.ylabel('sepal_width')
plt.savefig('KMeans_Iris.png')
plt.show()