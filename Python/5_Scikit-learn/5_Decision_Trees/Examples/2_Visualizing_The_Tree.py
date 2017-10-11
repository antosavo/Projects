import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from os import system

data = pd.read_csv('Iris.csv')

print 'Unique Species:', data['species'].unique()

colnames = data.columns.values
x = data[colnames[:4]]
y = data[colnames[4]]

model = DecisionTreeClassifier(criterion='entropy', max_depth=3)

model.fit(x, y)

export_graphviz(model, out_file = 'dtree.dot', class_names = data['species'].unique(), feature_names = colnames[:4])

system("dot -Tpng dtree.dot -o dtree.png")

