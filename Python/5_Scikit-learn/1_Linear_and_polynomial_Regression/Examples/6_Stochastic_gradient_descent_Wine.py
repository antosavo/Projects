import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('winequality-red.csv', sep=';')

Names = df.columns.values[0:-1]
#print "\nNames of all columns except the last one:\n", Names

x = df[Names]#the last column is the quality that is the y parameter, [0:-1] means all but not the last
y = df['quality']

x_train, x_test, y_train, y_test = train_test_split(x, y)
#By default, 25 percent of the data is assigned to the test set.

sx = x_train.std(axis=0)

#Standardize features by removing the mean and scaling to unit variance.
x_scaler = StandardScaler()
x_train = x_scaler.fit_transform(x_train)
x_test = x_scaler.transform(x_test)

print "mean x scaled:", x_train.mean(axis=0).astype(int)
print "std x scaled:", x_train.std(axis=0)

model = SGDRegressor(loss='squared_loss')
model.fit(x_train, y_train)

print 'R^2:', model.score(x_test, y_test)
print "Scaled Intercept= ", model.intercept_ #A in y = A + B*x
print "Scaled Coefficients= \n", model.coef_ #B in y = A + B*x

print "Coefficients= \n", model.coef_/sx
