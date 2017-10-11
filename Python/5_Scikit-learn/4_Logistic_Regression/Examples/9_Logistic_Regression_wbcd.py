import numpy as np
import pandas as pd
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.metrics import precision_score,recall_score, f1_score, make_scorer

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

x = df[features]
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6)

classifier = LogisticRegression()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

table = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predictions'])
print 'Crosstab:\n', table

print '\nAccuracy : ', classifier.score(x_test, y_test)

print 'Precision: ', precision_score(y_test, y_pred)

print 'Recall: ', recall_score(y_test, y_pred)

print 'F1: ', f1_score(y_test, y_pred)

def Map(x):
  return np.where(x==0,1,0)

print 'F1 0 is the positive class: ', f1_score(Map(y_test), Map(y_pred))

