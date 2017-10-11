import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestRegressor

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

model = RandomForestRegressor(n_estimators=100)

model.fit(x_train, y_train)

sf = pd.DataFrame({'Name':features,'Importance': model.feature_importances_})

print sf.sort_values('Importance',ascending=False)

print 'score:', model.score(x_test,y_test)