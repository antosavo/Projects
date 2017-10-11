import numpy as np
import pandas as pd
import pylab as plt
from sklearn.linear_model.logistic import LogisticRegression

x = np.array([[6, 1], [8, 2], [10, 3], [14, 4], [18, 5], [22,6],[26,7]])
y = np.array([0,0,0,0,1,1,1])

classifier = LogisticRegression()
classifier.fit(x, y)

print "Intercept= ", classifier.intercept_
print "Coefficients= ", classifier.coef_

print "Accuracy = #Correct/#Instances", classifier.score(x, y)

y_pred = classifier.predict(x)

table = pd.crosstab(y, y_pred, rownames=['Actual'], colnames=['Predictions'])
print table