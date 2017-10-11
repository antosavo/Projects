'''
Boston.xls is a data set on housing values in Boston.

CRIM: per capita crime rate by town 
ZN: proportion of residential land zoned for lots over 25,000 sq.ft. 
INDUS: proportion of non-retail business acres per town 
CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise) 
NOX: nitric oxides concentration (parts per 10 million) 
RM: average number of rooms per dwelling 
AGE: proportion of owner-occupied units built prior to 1940 
DIS: weighted distances to five Boston employment centres 
RAD: index of accessibility to radial highways 
TAX: full-value property-tax rate per $10,000 
PTRATIO: pupil-teacher ratio by town 
B: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town 
LSTAT: % lower status of the population 
MEDV: Median value of owner-occupied homes in $1000's
'''

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

df = pd.read_excel('Boston.xls')

print 'Some Data:\n', df.head()
print 'Shape:', df.shape
print 'Column Names:', df.columns.values
print 'Correlation with MEDV:\n', df.corr()['MEDV'].abs().sort_values(ascending=False)

colnames = df.columns.values
features = colnames[:13]
target = colnames[13]

x = df[features]
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(x, y)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print 'Some predictions= \n', y_pred[0:5]

print 'Intercept= ', model.intercept_ #A in y = A + B*x
print 'Coefficients= \n', model.coef_ #B in y = A + B*x
print 'R-squared= ', model.score(x_test, y_test)

plt.scatter(y_test, y_pred,color = "red")
plt.plot([0,50], [0,50], c='b')
plt.xlabel("y_True")
plt.ylabel("y_Predicted")
plt.axis([0,50,0,50])
#plt.legend()
plt.savefig("4_Boston.png")
plt.show()
