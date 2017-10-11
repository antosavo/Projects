import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x = [[6], [8], [10], [14],   [18]]
y = [[7], [9], [13], [17.5], [18]]

x_test = [[6], [8],[11], [16]]
y_test = [[8], [12], [15], [18]]

poly = PolynomialFeatures(degree=2)
poly.fit(x)

#x_p = poly.fit_transform(x) #x_p=[1, x, x*x]
x_p = poly.transform(x) #x_p=[1, x, x*x]
x_p_test = poly.transform(x_test) #x_p_test=[1, x, x*x]

print "x_p=", x_p

model = LinearRegression()
model.fit(x_p, y)

print "Intercept = ", model.intercept_[0] # a in y = a + b*x
print "Coefficient = ", model.coef_[0] # b in y = a + b*x
print "R-squared = ", model.score(x_p_test, y_test)
#For degree =2  R^2=0.87
#For degree =9  R^2=-0.09 over-fitting

x_fine = np.linspace(0, 26, 1000).reshape(1000, 1) #sklearn works with transposed vectors
x_fine_p = poly.transform(x_fine)

plt.scatter(x, y)
plt.plot(x_fine, model.predict(x_fine_p), c='r')
plt.title('Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0.,30.])
plt.ylim([0.,20.])
plt.savefig("3B_Polynomial_regression.png")
plt.show()