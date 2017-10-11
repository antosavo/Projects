#Random forest is a collection of regression trees. A random forest algorithm 
#creates trees at random and then averages the predictions of these trees.
#It is an algorithm for both classification and regression prediction.
#Random forest doesn't need a cross-validation. Instead, it uses something called Bagging.
#Suppose we want n observations in our training dataset T. Also, let's say there are m
#variables in the dataset. We decide to grow S trees in our forest. Each tree will be grown
#from a separate training dataset. So, there will be S training datasets. The training datasets
#are created by sampling n observations randomly with a replacement (n times).
#1. Take a random sample of size n.
#2. Take a random sample of the predictor variables.
#3. Construct a regression tree using the predictors chosen in the random sample in step 2. 
# Let it grow as much as it can. Do not prune the tree.
#4. The final predicted value for an observation is the average of the predicted values for
#that observation over all the trees. In the case of a classifier, the final class will be
#decided by a majority of votes.

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier #For categorical variables
from sklearn.ensemble import RandomForestRegressor #For continuous variables

data = pd.read_csv('Iris.csv')

print 'Some Data:\n', data.head()
print 'Unique Species:', data['species'].unique()

colnames = data.columns.values#.tolist()
print 'Column Names:', colnames

x = data[colnames[:4]]
y = data[colnames[4]]

x_train, x_test, y_train, y_test = train_test_split(x, y)
#By default, 25 percent of the data is assigned to the test set.

model = RandomForestClassifier(n_estimators=10)
#The n_estimators specifies the number of trees our random forest will have.

model.fit(x_train, y_train)

print "Features:", colnames[:4]
print "Feature importances:", model.feature_importances_
print "Score:",model.score(x_test, y_test)

y_pred = model.predict(x_test)

table = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predictions'])
print table
