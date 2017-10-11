#In one-hot encoding approach it is created a new dummy feature for each
#unique value in the nominal feature column. Here, we would convert the color
#feature into three new features: blue, green, and red. Binary values can then be
#used to indicate the particular color of a sample; for example, a blue sample can be
#encoded as blue=1, green=0, red=0.
import pandas as pd

df = pd.DataFrame([
	['green', 'M', 10.1, 'class1'],
	['red', 'L', 13.5, 'class2'],
	['blue', 'XL', 15.3, 'class1'],
	['red', 'S', 12.3, 'class2']
	],
	columns = ['color', 'size', 'price', 'classlabel'])

print 'df:\n', df

df2 = pd.get_dummies(df, columns=['color'])

print df2
