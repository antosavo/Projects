import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV

df = pd.read_csv('winequality-red.csv', sep=';')

print '\nSome Data:\n', df.head()
print '\nShape:', df.shape
print '\nColumn Names:', df.columns.values
print '\nMean for Classes:\n', df.groupby(df['quality']).mean()
print '\nCorrelation with quality:\n', df.corr()['quality'].order() #sort(inplace=False) #sort_values()

Names = df.columns.values[0:-1]#Names of all columns except the last one

x = df[Names]#the last column is the quality that is the y parameter, [:-1] means all but not the last
y = df['quality']

x_train, x_test, y_train, y_test = train_test_split(x, y)
#By default, 25 percent of the data is assigned to the test set.

model = svm.SVC(kernel='rbf')
parameters = {'gamma': np.arange(0.01,0.1,0.01), 'C': np.arange(1,3,0.1)}

grid_search = GridSearchCV(model, parameters, n_jobs=4, scoring='accuracy')
grid_search.fit(x_train, y_train)

print 'Best score:', grid_search.best_score_
print 'Best params:', grid_search.best_params_

y_pred = grid_search.predict(x_test)

plt.scatter(y_test, y_pred,color = "red")
plt.plot([2,9], [2,9], c='b')
plt.xlabel("y_True")
plt.ylabel("y_Predicted")
plt.axis([2,9,2,9])
#plt.legend()
plt.savefig("Wine.png")
plt.show()