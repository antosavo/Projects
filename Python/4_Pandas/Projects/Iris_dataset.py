import pandas as pd
import numpy as np
import matplotlib.pylab as plt

df = pd.read_csv('Iris.csv')
#df = pd.read_csv('Iris.csv', sep='\t', header=None)

print '\nSome Data:\n', df.head() #df.head(10)
print '\nShape:', df.shape #It founds the shape
print '\nNumber of Columns:', df.shape[1]
print '\nNumber of Rows:', df.shape[0]
print '\nColumn Names:', df.columns.values #df.columns.tolist()
print '\nColumn Names type (numpy.ndarray):', type(df.columns.values) #values converts to numpy.ndarray
print '\nFirst column:', df.columns.values[0]
print '\nIndexes:', df.index.values[0:10]
print '\nElement 7 petal_length:', df.loc[7,'petal_length']
print '\nElement (7,2):', df.iloc[7,2]
print '\nUnique Classes:', df['species'].unique()
print '\nPercentage Classes:\n', df['species'].value_counts(normalize=True)
print '\nMean for Classes:\n', df.groupby(df['species']).mean()
print '\nStd for Classes:\n', df.groupby(df['species']).std()
print '\nMean:\n', df.mean()
print '\nStd:\n', df.std()
print '\nMax:\n', df.max()
print '\nMin:\n', df.min()
print '\nDescription:\n', df.describe() #It describes the df
print '\nCorrelation:\n', df.corr() #sum((x_i-<x>)*(y_i-<y>))/sqrt(sum((x_i-<x>)**2)*sum((y_i-<y>)**2)) E [-1,1]
cr = df.corr()
print '\nMax Correlation:\n', cr[(cr>0.80) & (cr<1.0)] #and = & , or = | ,   
print '\nCorrelation petal_length - petal_width:\n', df.loc[:,['petal_length','petal_width']].corr() #It founds the correlations
print '\nCount values petal_length > 1:', df['petal_length'][df['petal_length'] > 1].count()
#print '\nFrame2 and 1 correlation:\n', df2.corrwith(df1)
#print '\nFrame with no Nan:\n', df.dropna()
#print '\nFrame repalce Nan with 0:\n', df.fillna(0)
#print '\nFrame without nan:\n', frame.replace(np.nan,0)
#print '\nFrame newcolors:\n', frame.replace({'rosso': 'red','verde': 'green'})
#print '\nConcat df 1 and 2 axis 0:\n', pd.concat([df1, df2])
#print '\nConcat df 1 and 2 axis 1:\n', pd.concat([df1, df2],axis=1)
#print '\nMerge df 1 and 2 on id:\n', pd.merge(df1,df2, on = 'id')
#print '\nMerge df 1 and 2 left on='id' and right on='sid':\n', pd.merge(df1, df2, left_on='id', right_on='sid')
#print '\nCrosstab:\n', pd.crosstab(y, y_pred, rownames=['names'], colnames=['items'])
print '\nMapping:', df['species'].map({'setosa':'red', 'versicolor':'blue', 'virginica':'green'}).unique()
for i in range(0,4):
  name = df.columns.values[i]
  print 'Correlation target with', name, ':', df['species'].map({'setosa':0, 'versicolor':1, 'virginica':2}).corr(df[name])

color_df = df['species'].map({'setosa':'red', 'versicolor':'blue', 'virginica':'green'}) 

plt.subplot( 2, 2, 1) #(plots per row, plots per col, position)
plt.scatter(df['petal_length'], df['petal_width'], c= color_df)
plt.xlabel('petal_length')
plt.ylabel('petal_width')

plt.subplot( 2, 2, 2)
plt.scatter(df['petal_length'], df['sepal_width'], c= color_df)
plt.xlabel('petal_length')
plt.ylabel('sepal_width')

plt.subplot( 2, 2, 3)
plt.scatter(df['petal_length'], df['sepal_length'], c= color_df)
plt.xlabel('petal_length')
plt.ylabel('sepal_length')

plt.subplot( 2, 2, 4)
plt.scatter(df['petal_width'], df['sepal_width'], c= color_df)
plt.xlabel('petal_width')
plt.ylabel('sepal_width')

plt.savefig('Iris.png')
plt.show()

df.to_csv('Iris_to_csv.csv', sep='\t', index=None, header=None, na_rep ='NaN')

'''
df = pd.read_csv('Iris.csv', sep='\t', header=None)

print '\nSome Data:\n', df.head()
print '\nShape:', df.shape
print '\nColumn Names:', df.columns.values
print '\nUnique Classes:', df['y'].unique()
print '\nPercentage y:\n', df['y'].value_counts(normalize=True)
print '\nHistogram y:\n', np.histogram(df['y'], bins=10, range=[0,10], normed=True)
print '\nDescription:\n', df.describe()
print '\nCorrelation:\n', df.corr()
print '\nMean for Classes::\n', df.groupby(df['y']).mean()
print '\nStd for Classes::\n', df.groupby(df['species']).std()
print '\nCorrelation y with x:', df['y'].corr(df['x']) # df.loc[:,['y','x']].corr()
print '\nCorrelation with y:\n', df.corr()['y'].order()
print '\nCrosstab:\n', pd.crosstab(y, y_pred, rownames=['names'], colnames=['items'])

df.to_csv('Iris_to_csv.csv', sep='\t', index=None, header=None)
'''

'''
Variance(x) =sum((x-<x>)**2)/(n-1)
std(x) = sqrt(var(x))
Covariance(x,y) = sum((x_i-<x>)*(y_i-<y>))/(n-1)
Correlation(x,y) = sum((x_i-<x>)*(y_i-<y>))/sqrt(sum((x_i-<x>)**2)*sum((y_i-<y>)**2))
'''
