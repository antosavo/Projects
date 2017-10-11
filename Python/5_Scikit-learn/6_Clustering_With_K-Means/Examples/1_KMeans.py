#Clustering is an unsupervised learning technique, it is used to find 
#groups of similar observations within a set of unlabeled data.
#K-Means assigns observations to one of K clusters.
#First, the clusters' centroids are initialized to random positions.
#Second, instances are assign to the closest centroids.
#Then we move the centroids to their assigned observations' mean location.
#The optimal values of K-Means' parameters are found by minimizing
#a cost function given by sum of distances from the centers.
#In k-means++ algorithm the initial centroids are placed far away from each other.
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

k = 2

model = KMeans(n_clusters=k, init ='k-means++')
model.fit(X)

print 'cluster centers:\n', model.cluster_centers_ 

print 'prediction c1:\n', model.predict(cluster1)

print 'prediction c2:\n', model.predict(cluster2)

print 'Cost function J =', model.inertia_ 

J = ((X - model.cluster_centers_[model.predict(X)])**2).sum().sum() 

print 'Cost function J (by hand)=', J 

#plt.scatter(X['x1'], X['x2'], c=model.predict(X), cmap = "cool", edgecolor = "none", s=50)

'''
color = []

for x in model.predict(X):
  if x == 0 :
    color.append('cyan')
  else :
    color.append('pink')
'''

color = pd.Series(model.predict(X)).map({0:'cyan', 1:'pink'})

plt.scatter(X[:,0], X[:,1], c= color, edgecolor = "none", s=50)
plt.scatter(model.cluster_centers_[0][0], model.cluster_centers_[0][1], marker='v', color ='blue', edgecolor = "none", s=80)
plt.scatter(model.cluster_centers_[1][0], model.cluster_centers_[1][1], marker='*', color ='red', edgecolor = "none", s=80)
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig("KMeans.png")
plt.show()
