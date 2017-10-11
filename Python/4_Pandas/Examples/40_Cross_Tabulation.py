import numpy as np
import pandas as pd

a = pd.Series(['tavern', 'tavern', 'tavern', 'tavern', 'bar', 'bar','bar', 'bar', 'tavern', 'tavern'])
b = pd.Series(['one', 'one', 'one', 'two', 'one', 'one', 'one', 'two', 'two', 'two'])

table = pd.crosstab(a, b, rownames=['Actual'], colnames=['Predictions'])
print table, '\n'

names = ["Alice", "Bob", "Mike"]
items = ["milk", "bread", "butter", "apples", "oranges"]

df = pd.DataFrame((names[i % 3], items[i % 5]) for i in range(100))

table2 = pd.crosstab(df[0] , df[1] , rownames=['names'], colnames=['items'])
print table2