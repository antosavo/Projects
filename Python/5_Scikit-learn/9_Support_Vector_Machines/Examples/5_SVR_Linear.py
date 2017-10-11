#SVR (Support Vector Regression)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm

x = np.array([1,2,3,4,5,6,7,8,9]).reshape(-1,1)
y = np.array([1.1,1.9,3.1,3.9,5.1,5.9,7.1,7.9,9.1]).reshape(-1,1)

model = svm.SVR(kernel='linear', C=1)
model.fit(x,y)

print "Parameters : \n", model.get_params

print "Intercept= ", model.intercept_[0] #A in y = A + B*x
print "Coefficient= ", model.coef_[0][0] #B in y = A + B*x
print "R-squared = ", model.score(x,y)#R^2(x,y) = 1 - {sum[(y(x)-y_model(x))^2]/sum[(y(x)-<y>)^2]} 

y_predict = model.predict(x)

plt.scatter(x, y, c ='red', s=60)
plt.plot(x, y_predict)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('SVR_linear.png')
plt.show()






