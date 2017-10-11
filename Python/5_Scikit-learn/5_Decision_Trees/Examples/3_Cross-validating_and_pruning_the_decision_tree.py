import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, cross_val_predict

data = pd.read_csv('Iris.csv')

print 'Some Data:\n', data.head()
print 'Unique Species:', data['species'].unique()

colnames = data.columns.values.tolist()
print 'Column Names:', colnames

x = data[colnames[:4]]
y = data[colnames[4]]

model = DecisionTreeClassifier(criterion='entropy', max_depth=3)

y_pred = cross_val_predict(model, x, y, cv=5)

table = pd.crosstab(y, y_pred, rownames=['Actual'], colnames=['Predictions'])
print table

scores = cross_val_score(model, x, y, cv=5, scoring='accuracy')
#scoring = ['accuracy', 'f1', 'mean_squared_error', 'precision', 'r2', 'recall']
print "<score> = ", scores.mean(), "\n", "scores = ", scores