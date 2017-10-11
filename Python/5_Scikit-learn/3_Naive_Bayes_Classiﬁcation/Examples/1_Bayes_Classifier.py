#The "naive" assumptions is: each feature is independent of every other feature 
#C_k = class k
#x = (x_1, x_2, ...x_n) instance with n features
#P(C_k) prior = (number of samples in the class) / (total number of samples)
#P(x_i, C_k) likelihood or feature's distribution
#The assumption for feature's distribution is called the event model of the Naive Bayes classifier.
#y = max[P(C_k)Prod(i=1,n)P(x_i,C_k)] , k E (1,2,3,..)
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt


cluster1 = pd.DataFrame(np.random.uniform(0.5, 1.5, (10, 2)), columns=['x1','x2'])
cluster2 = pd.DataFrame(np.random.uniform(3.5, 4.5, (10, 2)), columns=['x1','x2'], index = np.arange(10,20))

X = pd.concat([cluster1, cluster2])
y = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]

model = GaussianNB()
model.fit(X,y)

print "Accuracy:", model.score(X,y)

plt.scatter(X['x1'], X['x2'], c=model.predict(X), cmap = "cool", edgecolor = "none", s=50)
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig("Bayes_Classifier.png")
plt.show()
