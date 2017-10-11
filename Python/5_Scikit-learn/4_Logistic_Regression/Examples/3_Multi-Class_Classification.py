import numpy as np
import pandas as pd
import pylab as plt
from sklearn.linear_model.logistic import LogisticRegression

x = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9],[10], [11], [12] ])
y = np.array([0,0,0,0,1,1,1,1,1,2,2,2])

classifier = LogisticRegression()
classifier.fit(x, y)

print "Intercept= ", classifier.intercept_
print "Coefficients= ", classifier.coef_

print "Accuracy = #Correct/#Instances", classifier.score(x, y)

prob = classifier.predict_proba(x)

print "Probability:\n", prob

y_pred = classifier.predict(x)

table = pd.crosstab(y, y_pred, rownames=['Actual'], colnames=['Predictions'])
print table
