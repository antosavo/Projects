import pandas as pd
import matplotlib.pylab as plt
from sklearn.linear_model import ElasticNet
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import train_test_split

df = pd.read_csv('winequality-red.csv', sep=';')

#print '\nSome Data:\n', df.head()
print '\nShape:', df.shape
print '\nColumn Names:', df.columns.values
#print '\nMean for Classes:\n', df.groupby(df['quality']).mean()
print '\nCorrelation with quality:\n', df.corr()['quality'].order() #sort(inplace=False) #sort_values()

Names = df.columns.values[0:-1]#Names of all columns except the last one

#By default, train_test_split() assigns 75 percent of the samples to the
#training set and allocates the remaining 25 percent of the samples to the test set.
x_train, x_test, y_train, y_test = train_test_split(df[Names], df['quality'])

model = ElasticNet() 

#We specified the hyperparameter space for the grid search.
parameters = {'alpha': (0.0001, 0.0025, 0.0050, 0.0075, 0.0100), 'l1_ratio':(0.5,1.0)}

grid_search = GridSearchCV(model, parameters, cv =5, scoring='r2')
#scoring = ['accuracy', 'f1', 'mean_squared_error', 'precision', 'r2', 'recall']

grid_search.fit(x_train, y_train)

print 'Best score:', grid_search.best_score_
print 'Best params:', grid_search.best_params_

#Test

model2 = grid_search.best_estimator_

y_pred = model2.predict(x_test)

print 'Some Predictions:', y_pred[0:5]

print 'Test Score:', model2.score(x_test,y_test)
