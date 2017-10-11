#SVR (Support Vector Regression)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm

x = np.array([1,2,3,4,5,6,7,8,9]).reshape(-1,1)
y = x*x + np.random.randn(9,1)

model = svm.SVR(kernel='poly', C=1, degree=2)
model.fit(x,y)

print "Intercept= ", model.intercept_[0] #Constants in decision function.
print "R-squared = ", model.score(x,y)#R^2(x,y) = 1 - {sum[(y(x)-y_model(x))^2]/sum[(y(x)-<y>)^2]} 

y_predict = model.predict(x)

plt.scatter(x, y, c ='red', s=60)
plt.plot(x, y_predict)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('SVR_poly.png')
plt.show()






