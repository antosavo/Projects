#Classifing the sentiments of phrases taken from movie reviews
#in the Rotten Tomatoes data set.
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import train_test_split, cross_val_score

df = pd.read_csv('train.tsv', sep ='\t')

print '\nShape:', df.shape
print '\nColumn Names:', df.columns.values
print '\nSome data:\n', df.head(10)
#print '\nSome data:\n', df.loc[:,['Sentiment','Phrase']].head(10)
print '\nUnique Classes for Sentiment:', df['Sentiment'].unique()
print '\nPercentage Sentiment:\n', df['Sentiment'].value_counts(normalize=True)
print '\nSentiment description:\n', df['Sentiment'].describe()
    
X = df['Phrase']
y = df['Sentiment'].as_matrix()

X_train_raw, X_test_raw, y_train, y_test = train_test_split(X, y, train_size=0.5)

#We fit and transform both the training and test messages.
vectorizer = TfidfVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print '\n'

for i in range(0,10):
  print 'Prediction:', y_pred[i] , 'Message:', list(X_test_raw)[i]

#Accuracy = #Correct_Predictions/#Predictions

print '\nAccuracy = ', classifier.score(X_test, y_test)

table = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predictions'])
print 'Crosstab:\n', table






