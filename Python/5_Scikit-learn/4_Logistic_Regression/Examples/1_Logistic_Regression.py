#Logistic regression can be used for binary classification, a task in which an
#instance must be assigned to one of two classes.
#LR uses a logistic function to relate a linear combination of the explanatory
#variables to a value between zero and one which corresponds to the chance to belong to one of the two classes.
#The predicted probability can then simply be converted into a binary outcome via a step function.
import numpy as np
import pandas as pd
import pylab as plt
from sklearn.linear_model.logistic import LogisticRegression

x = np.array([[0],[1],[2],[3],[4],[5],[6]])
y = np.array([0,0,0,0,1,1,1])

classifier = LogisticRegression()
classifier.fit(x, y)

b_0 = classifier.intercept_[0]
b_1 = classifier.coef_[0][0]
print "Intercept= ", b_0
print "Coefficient= ", b_1

print "Accuracy = #Correct/#Instances", classifier.score(x, y)

y_pred = classifier.predict(x)

table = pd.crosstab(y, y_pred, rownames=['Actual'], colnames=['Predictions'])
print table

x_fine = np.linspace(-2,10,20)
y_fine = 1/(1+np.exp(-b_0 - b_1*x_fine))

plt.plot(x_fine, y_fine )
plt.xlabel('x')
plt.ylabel('y')
plt.show()
