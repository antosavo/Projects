#Regularization is a collection of techniques that can be used to prevent over-fitting.
#Regularization adds information to a problem, often in the form of a penalty.
#Ridge regression (L2) is a penalized model where we add the squared sum of
#the weights to our cost function.
#By increasing the value of the hyperparameter alpha, we increase the regularization
#strength and shrink the weights of our model. 
#Hyperparameters are parameters of the model that are not learned automatically and must be set
#manually. Note that we don't regularize the intercept term w0.
import pandas as pd
import matplotlib.pylab as plt
from sklearn.linear_model import Ridge
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import train_test_split

df = pd.read_csv('winequality-red.csv', sep=';')

#print '\nSome Data:\n', df.head()
print '\nShape:', df.shape
print '\nColumn Names:', df.columns.values
#print '\nMean for Classes:\n', df.groupby(df['quality']).mean()
print '\nCorrelation with quality:\n', df.corr()['quality'].order() #sort(inplace=False) #sort_values()

Names = df.columns.values[0:-1]#Names of all columns except the last one

x_train, x_test, y_train, y_test = train_test_split(df[Names], df['quality'])

model = Ridge() #model = Ridge(alpha=1.0)

#We specified the hyperparameter space for the grid search.
parameters = {'alpha': (0.000, 0.025, 0.050, 0.075, 0.100)}

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
