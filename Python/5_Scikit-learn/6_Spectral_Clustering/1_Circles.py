'''
k-means clustering partitions n observations into k clusters in which each observation belongs to the cluster with the nearest mean. The algoritm doesn't work if clusters are separated by nonlinear boundaries.
In Spectral Clustering each observation belongs to the cluster to which is better connected. The relationship between data points is rapressented by a graph, each edge is weighted by a similarity metric, the best partitions are the one where the weights that connect different clusters are as small as possible.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.cluster import SpectralClustering

x, y = make_circles(n_samples=1000, noise=0.1, factor=0.2)

model = SpectralClustering(n_clusters=2, affinity='nearest_neighbors')

#print model.fit_predict(x)

color = pd.Series(model.fit_predict(x)).map({ 0:'red', 1:'blue'})

plt.scatter(x[:,0], x[:,1], c= color, marker='o')

plt.xlabel('x1')
plt.ylabel('x2')
plt.savefig('Circles.png')
plt.show()
