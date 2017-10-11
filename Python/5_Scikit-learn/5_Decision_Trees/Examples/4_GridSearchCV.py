import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.grid_search import GridSearchCV

data = pd.read_csv('Iris.csv')

print 'Some Data:\n', data.head()
print 'Unique Species:', data['species'].unique()

colnames = data.columns.values.tolist()
print 'Column Names:', colnames

x = data[colnames[:4]]
y = data[colnames[4]]

x_train, x_test, y_train, y_test = train_test_split(x, y)
#By default, 25 percent of the data is assigned to the test set.

model = DecisionTreeClassifier(criterion='entropy')

#We specified the hyperparameter space for the grid search.
parameters = {'max_depth': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}

grid_search = GridSearchCV(model, parameters, cv =5, scoring='accuracy')
#scoring = ['accuracy', 'f1', 'mean_squared_error', 'precision', 'r2', 'recall']

grid_search.fit(x_train, y_train)

print 'Best score:', grid_search.best_score_
print 'Best params:', grid_search.best_params_

y_pred = grid_search.predict(x_test)

table = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predictions'])
print table

print 'Test Score:', grid_search.score(x_test,y_test)
