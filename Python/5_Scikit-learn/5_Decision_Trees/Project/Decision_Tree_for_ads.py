#We will train a decision tree classifier using the Internet Advertisements Data Set 
#from http://archive.ics.uci.edu/ml/datasets/Internet+Advertisements .

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('ad.data',header=None)

data.replace(to_replace=' *\?', value=-1, regex=True, inplace=True)

print '\nSome Data:\n', data.head()
print '\nShape:', data.shape

N = data.shape[1] -1
print '\nUnique Classes:', data[N].unique()
print '\nPercentage y:\n', data[N].value_counts(normalize=True)

colnames = data.columns.values

x = data[colnames[:N]]
y = data[colnames[N]].map({'ad.':0, 'nonad.':1})

x_train, x_test, y_train, y_test = train_test_split(x, y)
#By default, 25 percent of the data is assigned to the test set.

model = DecisionTreeClassifier(criterion='entropy', max_depth=150)

model.fit(x_train, y_train)

print "Score = ", model.score(x_test,y_test)

y_pred = model.predict(x_test)

table = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predictions'])
print table