import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

#Crerate df
df = pd.DataFrame(np.arange(16).reshape(4,4),
	index=['white','black','red','blue'],
	columns=['up','down','right','left'])
print "df:\n", df

#Save JSON file (JavaScript Object Notation)
df.to_json('frame.json')

#Read JSON file
df2 = pd.read_json('frame.json')
print "df2:\n", df2

#Normalization: convert the structure dict file in tabular form.
file = open('books.json','r')
text = file.read()
print "json text:\n", text
text = pd.json.loads(text)
print "json df book:\n", json_normalize(text,'books')
print "json df:\n", json_normalize(text,'books',['writer','nationality'])






