import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

x = np.array([[6, 2], [8, 1], [10, 0], [14, 2], [18, 0]])
y = np.array([[7],[9],[13],[17.5], [18]])
#d = np.array([[6, 2, 7], [8, 1, 9], [10, 0, 13], [14, 2, 17.5], [18, 0, 18]])
#x = d[:,0:2]
#y = d[:, 2]
#df = pd.DataFrame({'0':[6,8,10,14,18],
#		   '1':[2,1,0,2,0],
#		   '2':[7,9,13,17.5,18]})
#c = df.columns.values
#x =df[c[0:2]]
#y =df[c[2]]

model = LinearRegression()
model.fit(x, y)

x_test = np.array([[8, 2], [9, 0], [11, 2], [16, 2], [12, 0]])
y_test = np.array([[11],[8.5], [15],[18],[11]])

predictions = model.predict(x_test)

N = np.size(predictions)

for i in range(0,N):
  print "Predicted:", predictions[i], "Target:", y_test[i]


print "Intercept = ", model.intercept_[0] #A in y = A + B*x
print "Coefficients = ", model.coef_[0] #B in y = A + B*x
print "R-squared = ", model.score(x_test, y_test)

