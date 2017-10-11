#If K is not specified by the problem's context, the optimal number of clusters can
#be estimated using a technique called the elbow method. The elbow method plots
#the value of the cost function produced by different values of K . As K increases,
#the average distortion will decrease; each cluster will have fewer constituent
#instances, and the instances will be closer to their respective centroids. However,
#the improvements to the average distortion will decline as K increases. The value
#of K at which the improvement to the distortion declines the most is called the
#elbow.
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale


cluster1 = pd.DataFrame(np.random.uniform(0.5, 1.5, (10, 2)), columns=['x1','x2'])
#print cluster1
cluster2 = pd.DataFrame(np.random.uniform(3.5, 4.5, (10, 2)), columns=['x1','x2'], index = np.arange(10,20))
#print cluster2
X = scale(pd.concat([cluster1, cluster2]))
#print "\nconcat cluster1 and cluster2:\n", X

K = np.arange(1, 10)
J = []

for k in K:
  model = KMeans(n_clusters=k)
  model.fit(X)
  J.append(model.inertia_)

plt.plot(K, J, 'bx-')
plt.xlabel('clusters K')
plt.ylabel('cost function J')
plt.savefig('Elbow_Method.png')
plt.show()