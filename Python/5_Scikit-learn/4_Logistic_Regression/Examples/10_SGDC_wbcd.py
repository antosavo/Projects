'''
Stochastic gradient descent Classifier (SGDC)
The gradient of the loss is estimated each sample at a time.
With streaming data SGD allows on-line learning calling the partial_fit method on individual
samples.
For best results the data should have zero mean and unit variance.
loss = 'hinge' ---> SVC
loss = 'log'   ---> LR
'''
import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
from sklearn.linear_model import SGDClassifier
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.metrics import f1_score

df = pd.read_csv('Breast_cancer_wisconsin.csv').replace('?',np.nan)#.dropna()

df = df.fillna(df.median())

print '\nShape:', df.shape
print '\nColumn Names:', df.columns.values
print '\nSome data:\n', df.head(10)
print '\nUnique Classes:', df['class'].unique()
print '\nPercentage for class:\n', df['class'].value_counts(normalize=True)
print '\nClasses description:\n', df['class'].describe()
print '\nCorrelation with class:\n', df.corr()['class'].abs().sort_values(ascending=False)

colnames = df.columns.values

features = colnames[0:9]
target = colnames[9]

x = scale(df[features])
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6, random_state=1)

classifier = SGDClassifier(loss='log',random_state=1)
classifier.fit(x_train, y_train)
classifier.partial_fit(x_test[42,:],[y_test[42]]) #online learning

y_pred = classifier.predict(x_test)

table = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predictions'])
print 'Crosstab:\n', table

print '\nAccuracy : ', classifier.score(x_test, y_test)

print 'F1: ', f1_score(y_test, y_pred)