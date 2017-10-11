import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.grid_search import GridSearchCV

data = pd.read_csv('Iris.csv')

print 'Some Data:\n', data.head()
print 'Unique Species:', data['species'].unique()

colnames = data.columns.values
print 'Column Names:', colnames

x = data[colnames[0:2]]
y = data[colnames[4]]

model = svm.SVC(kernel='poly') #Support Vector Classification

parameters = {'degree': (2, 3, 4, 5), 'C': (1, 3, 5, 10)}

grid_search = GridSearchCV(model, parameters, n_jobs=4, scoring='accuracy')

grid_search.fit(x, y)

print 'Best score:', grid_search.best_score_
print 'Best params:', grid_search.best_params_

y_pred = grid_search.predict(x)

table = pd.crosstab(y, y_pred, rownames=['Actual'], colnames=['Predictions'])
print table

colors = y.map({'setosa':'red', 'versicolor':'blue', 'virginica':'green'})

max1 = x['sepal_length'].max() +0.5
max2 = x['sepal_width'].max() +0.5

X1, X2 = np.mgrid[0:max1:0.01, 0:max2:0.01]

N = X1.shape[0]*X1.shape[1]

X1 = X1.reshape(1,N)
X2 = X2.reshape(1,N)

Z = np.concatenate([X1,X2])

Z = grid_search.predict(Z.T)

Z = pd.Series(Z).map({'setosa':'pink', 'versicolor':'cyan', 'virginica':'yellow'}) # 0 or 1

plt.scatter(X1, X2, c = Z, marker = ".", edgecolor = "none")
plt.scatter(x['sepal_length'], x['sepal_width'], c = colors, s=60)
plt.xlim([3,max1])
plt.xlabel('sepal_length')
plt.ylim([1,max2])
plt.ylabel('sepal_width')
plt.savefig('SVC_Iris.png')
plt.show()







