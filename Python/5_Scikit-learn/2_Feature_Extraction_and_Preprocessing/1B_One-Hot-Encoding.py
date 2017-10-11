#In one-hot encoding approach it is created a new dummy feature for each
#unique value in the nominal feature column. Here, we would convert the color
#feature into three new features: blue, green, and red. Binary values can then be
#used to indicate the particular color of a sample; for example, a blue sample can be
#encoded as blue=1, green=0, red=0.
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.DataFrame([
	['green', 'M', 10.1, 'class1'],
	['red', 'L', 13.5, 'class2'],
	['blue', 'XL', 15.3, 'class1'],
	['red', 'S', 12.3, 'class2']
	],
	columns = ['color', 'size', 'price', 'classlabel'])

print 'df:\n', df

vectorizer = CountVectorizer()
vectorizer.fit(df['color'])

y = vectorizer.transform(df['color']).toarray()#.todense()

print 'Encoded Vector:\n', y
print 'Vocabulary:', vectorizer.vocabulary_
print 'Inverse Encoding:\n', vectorizer.inverse_transform(y)
