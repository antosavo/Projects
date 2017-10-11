import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split

df = pd.read_excel('Boston.xls')

print 'Some Data:\n', df.head()
print 'Shape:', df.shape
#print 'Column Names:', df.columns.values
#print 'Correlation with MEDV:\n', df.corr()['MEDV'].abs().sort_values(ascending=False)

colnames = df.columns.values
features = colnames[:13]
target = colnames[13]

x = df[features]
y = df[target]

model = Pipeline([ ('poly', PolynomialFeatures(degree=2) ), ('lr', LinearRegression() )] ) #poly__degree

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

model.fit(x_train, y_train)

print 'R-squared= ', model.score(x_test, y_test)