import numpy as np
import pandas as pd
import pylab as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split, cross_val_score

df = pd.read_csv('SMSSpamCollection.dat', delimiter='\t', header=None)

print df.head()
print 'Shape:', df.shape #It founds the shape
print 'Percentage Classes:', df[0].value_counts(normalize=True)
print 'Number of spam messages:', df[df[0] == 'spam'][0].count()
print 'Number of ham messages:', df[df[0] == 'ham'][0].count()

#By default, train_test_split() assigns 75 percent of the samples to the
#training set and allocates the remaining 25 percent of the samples to the test set.
X_train_raw, X_test_raw, y_train, y_test = train_test_split(df[1], df[0])

#We fit d transform both the training and test messages.
vectorizer = TfidfVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)

classifier = MultinomialNB()
classifier.fit(X_train, y_train)

print 'Accuracy = #Correct_Predictions/#Predictions', classifier.score(X_test, y_test)

####

y_pred = classifier.predict(X_test)

table = pd.crosstab(pd.Series(y_test).map({'spam':0,'ham':1}), pd.Series(y_pred).map({'spam':0,'ham':1}), rownames=['Actual'], colnames=['Predictions'])
print 'crosstab:\n', table

####

for i in range(0,10):
  print 'Prediction:', y_pred[i] , 'Message:', list(X_test_raw)[i]

####

plt.matshow(table, cmap = 'Blues') #to plot matrix value in color map
plt.title('Confusion matrix')
plt.colorbar()#.set_ticks([0,2])
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.savefig('Confusion_matrix.png')
plt.show()