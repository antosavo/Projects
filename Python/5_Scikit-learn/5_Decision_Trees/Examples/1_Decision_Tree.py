#The purpose of this exercise will be to classify the flowers as belonging to one of the three species based on the dimensions.
#This algorithm using entropy and information gain is called ID3 algorithm, and can be
#summarized as follows:
#1.Calculate the initial entropy of the system based on the target variable.
#2.Calculate the information gains for each candidate variable for a node. Select the
#  variable that provides the maximum information gain as a decision node.
#3.Repeat step 2 for each branch (value) of the node (variable) identified in step 2. The
#  newly identified node is termed as leaf node.
#4.Check whether the leaf node classifies the entire data perfectly. If not, repeat the
#  steps from step 2 onwards. If yes, stop.

#Continuous numerical variables can also be used as a predictor variable while creating a decision tree, by defining thresholds.
#1.Sort the dataset based on the numerical variable in ascending order.
#2.Mark the numerical variable ranges where there is a transitions from one category to another.
#3.Corresponding to each transition in category, there will be one threshold. 

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('Iris.csv')

print 'Some Data:\n', data.head()
print 'Unique Species:', data['species'].unique()

colnames = data.columns.values #.tolist()
print 'Column Names:', colnames

x = data[colnames[:4]]
y = data[colnames[4]]

x_train, x_test, y_train, y_test = train_test_split(x, y)
#By default, 25 percent of the data is assigned to the test set.

model = DecisionTreeClassifier(criterion='entropy', max_depth=3)

model.fit(x_train, y_train)

print "Features:", colnames[:4]
print "Feature importances:", model.feature_importances_

y_pred = model.predict(x_test)

table = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predictions'])
print table

print "Score = ", model.score(x_test,y_test)