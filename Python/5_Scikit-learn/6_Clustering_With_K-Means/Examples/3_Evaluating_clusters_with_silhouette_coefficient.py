#The silhouette coefficient is a measure of the compactness and separation of the clusters. 
#It increases as the quality of the clusters increase; 
#it is large for compact clusters that are far from each other and small for large,
#overlapping clusters.
#s = ba/max(a,b)
#a is the mean distance between the instances in the cluster. b is the mean distance
#between the instance and the instances in the next closest cluster.

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

data = {'x1' : [1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9],
	'x2' : [1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3]}

X = scale(pd.DataFrame(data))

K = np.arange(2, 8)
S = []

for k in K:
  model = KMeans(n_clusters=k)
  model.fit(X)
  S.append(metrics.silhouette_score(X, model.predict(X), metric='euclidean')) #the min k is 2

plt.plot(K, S, 'bx-')
plt.xlabel('clusters K')
plt.ylabel('Silhouette Coefficient S')
plt.savefig('Silhouette_Coefficient.png')
plt.show()

plt.clf()

model = KMeans(n_clusters=3)
model.fit(X)

plt.scatter(X[:,0], X[:,1], c=model.predict(X), cmap = "cool", edgecolor = "none", s=50)
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig("Silhouette_Coefficient_k_3.png")
plt.show()