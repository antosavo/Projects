import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import cross_val_score, cross_val_predict

df = pd.read_csv('SMSSpamCollection.dat', delimiter='\t', header=None)

print df.head()
print '\nShape:', df.shape #It founds the shape

print 'Number of spam messages:', df[df[0] == 'spam'][0].count()
print 'Number of ham messages:', df[df[0] == 'ham'][0].count()

x = df[1]
y = df[0].map({'spam':0,'ham':1})

#We fit d transform both the training and test messages.
vectorizer = TfidfVectorizer(stop_words='english')
x = vectorizer.fit_transform(x)

classifier = LogisticRegression(penalty='l1', C=1.0)

#Accuracy = #Correct_Predictions/#Predictions
scores = cross_val_score(classifier, x, y, cv=5)
print "Accuracy = ", np.mean(scores)

y_pred = cross_val_predict(classifier, x, y, cv=5)

table = pd.crosstab(y, y_pred, rownames=['Actual'], colnames=['Predictions'])
print 'Crosstab Accuracy:\n', table