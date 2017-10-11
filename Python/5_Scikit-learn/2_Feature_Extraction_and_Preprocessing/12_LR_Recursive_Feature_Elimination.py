'''
Given an external estimator that assigns weights to features, recursive feature elimination (RFE) selects 
the most relevant features for the estimator. 
First, the estimator is trained on the initial set of features. Then, k features whose absolute weights are 
the smallest are eliminated. 
That procedure is recursively repeated until the desired number n of features is reached.
n = d -k*n_steps
'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE

df = pd.read_csv('winequality-red.csv', sep=';')

Names = df.columns.values[0:-1]#Names of all columns except the last one

x = df[Names]#the last column is the quality that is the y parameter, [:-1] means all but not the last
y = df['quality']

x_train, x_test, y_train, y_test = train_test_split(x, y)
#By default, 25 percent of the data is assigned to the test set.

#Standardize features by removing the mean and scaling to unit variance.
x_scaler = StandardScaler()
x_train = x_scaler.fit_transform(x_train)
x_test = x_scaler.transform(x_test)

model = LinearRegression()

selector = RFE(model, 2)
selector.fit(x_train, y_train)

x_train = selector.transform(x_train)
x_test = selector.transform(x_test)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print 'Some predictions= \n', y_pred[0:5]

print 'Intercept= ', model.intercept_ #A in y = A + B*x
print 'Coefficients= \n', model.coef_ #B in y = A + B*x
print 'R-squared= ', model.score(x_test, y_test)

plt.scatter(y_test, y_pred,color = "red")
plt.plot([0,10], [0,10], c='b')
plt.xlabel("y_True")
plt.ylabel("y_Predicted")
plt.axis([0,10,0,10])
#plt.legend()
plt.savefig("10_Wine.png")
plt.show()
