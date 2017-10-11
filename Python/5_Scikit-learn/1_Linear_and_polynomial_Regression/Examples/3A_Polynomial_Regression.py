import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([6, 8, 10, 14, 18]).reshape(-1, 1)#sklearn works with transposed vectors
y = np.array([7, 9, 13, 17.5, 18]).reshape(-1, 1)

x_test = np.array([6, 8,11, 16]).reshape(-1, 1)
y_test = np.array([8, 12, 15, 18]).reshape(-1, 1)

x_p = np.concatenate((x, x**2), axis=1)
x_p_test = np.concatenate((x_test, x_test**2), axis=1)

model = LinearRegression()
model.fit(x_p, y)

print "Intercept = ", model.intercept_[0] # a in y = a + b*x + c*x**2
print "Coefficients =", model.coef_[0] # b,c in y = a + b*x + c*x**2
print "R-squared = ", model.score(x_p_test, y_test)

x_fine = np.linspace(0, 26, 1000).reshape(1000, 1) #sklearn works with transposed vectors
x_fine_p = np.concatenate((x_fine, x_fine**2), axis=1)

plt.scatter(x, y)
plt.plot(x_fine, model.predict(x_fine_p), c='r')
plt.title('Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0.,30.])
plt.ylim([0.,20.])
plt.savefig("3A_Polynomial_regression.png")
plt.show()