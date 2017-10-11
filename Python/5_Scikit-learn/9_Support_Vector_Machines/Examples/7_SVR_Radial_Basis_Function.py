#SVR (Support Vector Regression)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from scipy.stats import norm
from scipy.optimize import curve_fit

x = np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]).reshape(-1,1)
y = norm( 5, 1).pdf(x) + 0.01*np.random.randn(9,1)

model = svm.SVR(kernel='rbf', C=1e4, gamma=0.5) #gamma=1/(2*sigma^2)
model.fit(x,y)

print "Intercept= ", model.intercept_[0] #Constants in decision function.
print "R-squared = ", model.score(x,y)#R^2(x,y) = 1 - {sum[(y(x)-y_model(x))^2]/sum[(y(x)-<y>)^2]} 

y_predict = model.predict(x)

#def gauss_function(x, a, x0, sigma):
#    return a*np.exp(-(x-x0)**2/(2*sigma**2))
def gauss_function(x, a, b):
    return norm(a,b).pdf(x)

params, cov = curve_fit(gauss_function, x.T[0], y.T[0])

plt.scatter(x, y, c ='red', s=60, label = 'data')
plt.plot(x, y_predict, label = 'prediction SVR')
plt.plot(x.T[0], gauss_function(x.T[0],*params), linestyle= "--", label = "fit scipy") #f(x,*params)=f(x,a,b,c)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('SVR_rbf.png')
plt.show()






