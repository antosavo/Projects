#Linear regression is a ML algorithm used when the value to be predicted is a continuous variable. 
#In LR the relationship between the features and the response variable (target) is approximated 
#with a straight line.
#The weights of the linear equation are found minimizing a cost function.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([6, 8, 10, 14, 18]).reshape(-1, 1) #sklearn works with transposed vectors
y = np.array([7, 9, 13, 17.5, 18]).reshape(-1, 1)
#x = np.array([[6], [8], [10], [14], [18]])
#y = np.array([[7], [9], [13], [17.5], [18]])
#df = pd.DataFrame({0:[6, 8, 10, 14, 18], 1:[7, 9, 13, 17.5, 18]})
#x = df[[0]] #sklearn works with transposed vectors
#y = df[[1]]

x_test = np.array([8, 9, 11, 16, 12]).reshape(-1,1)
y_test = np.array([11, 8.5, 15, 18, 11]).reshape(-1,1)

model = LinearRegression()
model.fit(x,y)
y_model = model.predict(x)

print "Intercept = ", model.intercept_[0] #A in y = A + B*x
print "Coefficient = ", model.coef_[0][0] #B in y = A + B*x
 
print "R-squared = ", model.score(x_test,y_test)#It says how good is the model R^2(x,y) = 1 - {sum[(y(x)-y_model(x))^2]/sum[(y(x)-<y>)^2]} 
#It is needed a set of test data for this

plt.plot(x, y, label = "data", linestyle=" ", marker = "o", color = "red")
plt.plot(x, y_model, label = "model", linestyle="-", color = "green")
plt.xlabel("x")
plt.ylabel("y")
plt.axis([0,25,0,25])
plt.legend()
plt.savefig("1_Linear_regression.png")
plt.show()



