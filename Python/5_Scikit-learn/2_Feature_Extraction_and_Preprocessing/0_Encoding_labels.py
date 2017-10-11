#So far, we have only been working with numerical values. However, it is not
#uncommon that real-world datasets contain one or more categorical feature columns.(ex.colors)
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame([
	['green', 'M', 10.1, 'class1'],
	['red', 'L', 13.5, 'class2'],
	['blue', 'XL', 15.3, 'class1'],
	['red', 'S', 12.3, 'class2']
	],
	columns = ['color', 'size', 'price', 'classlabel'])

print 'df:\n', df

#Encoding Using LabelEncoder()
le = LabelEncoder()
le.fit(df['color'])

y = le.transform(df['color'])

print 'Encoded colors:', y
print 'Inverse Encoding:', le.inverse_transform(y)

#Pandas Manual Encoding
print '\nPandas Encoding Manual:', df['color'].map({'green':0,'red':1,'blue':2}).values

#Pandas Encoding
dictionary ={}

colors = df['color'].unique()

for color in enumerate(colors):
  dictionary.update({color[1]:color[0]}) #color[0] = index and color[1] = label

print '\nPandas Encoding:', df['color'].map(dictionary).values

#
print '\nDictionary:', dictionary
print 'Enumerate colors:', dict(enumerate(colors))


