#The target variable in the case of a regression tree is a continuous numerical
#variable, unlike decision trees where the target variable is a categorical variable.
#A regression tree is similar to a decision tree because the algorithm behind them is more or
#less the same; the node is split into subnodes based on certain criteria. The criterion
#of a split, in this case, is the maximum Reduction in Variance;
#A stepwise summary of the regression tree algorithm is as follows:
#1.Start with a single node, that is, all the observations, calculate the mean, and then the
# variance of the target variable.
#2.Calculate the reduction in variance caused by each of the variables that are potential
# candidates for being the next node. Choose the variable that provides the maximum reduction in the variance as
# the node.
#3.For each leaf node, check whether the maximum reduction in the variance provided
# by any of the variables is less than a set threshold, or the number of observations in a
# given node is less than a set threshold. If one of these criterions is satisfied, stop. If
# not, repeat step 2.

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import train_test_split

data = pd.read_excel('Boston.xls')

print 'Some Data:\n', data.head()
print 'Shape:', data.shape

colnames = data.columns.values
print 'Column Names:', colnames

features = colnames[:13]
target = colnames[13]
x = data[features]
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y)

model = DecisionTreeRegressor(max_depth=3)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print "Some Prediction:",y_pred[0:5]
print "Score:",model.score(x_test, y_test)
print "Features:", colnames[:13]
print "Feature importances:", model.feature_importances_
