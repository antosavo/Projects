import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import train_test_split, cross_val_score

df = pd.read_csv('sms.csv')

print df.head()
print "\nShape:", df.shape #It founds the shape

#By default, train_test_split() assigns 75 percent of the samples to the
#training set and allocates the remaining 25 percent of the samples to the test set.
X_train_raw, X_test_raw, y_train, y_test = train_test_split(df['message'], df['label'])

#We fit d transform both the training and test messages.
vectorizer = TfidfVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)

predictions = classifier.predict(X_test)

for i in range(0,10):
  print 'Prediction:', predictions[i] , 'Message:', list(X_test_raw)[i]



#Accuracy = #Correct_Predictions/#Predictions
scores = cross_val_score(classifier, X_train, y_train, cv=5)
print "Mean Accuracy =", np.mean(scores)
print "All Accuracies =", scores

#Precision P = TP/(TP + FP)
precisions = cross_val_score(classifier, X_train, y_train, cv=5, scoring='precision')
print "Mean Precision =", np.mean(precisions)
print "All Precisions =", precisions

#Recall R = TP/(TP + FN)
recalls = cross_val_score(classifier, X_train, y_train, cv=5, scoring='recall')
print "Mean Recall =", np.mean(recalls)
print "All Recalls =", recalls

#F1 measure
#F1 = 2PR/(P+R)
f1s = cross_val_score(classifier, X_train, y_train, cv=5, scoring='f1')
print 'Mean F1:', np.mean(f1s)
print 'All F1:', f1s

