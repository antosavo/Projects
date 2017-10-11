import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

x = np.arange(0,1,0.01).reshape(100, 1)
y = 2*( np.arange(0,1,0.01) + 0.001*np.random.normal(100))**2 

x_train, x_test, y_train, y_test = train_test_split(x, y)

# for 3 hidden_layer_sizes = (100,100,100) #default (100)
# solver : {'lbfgs','sgd', 'adam'}, default 'adam'
# learning_rate_init : double, default 0.001
# activation : 'identity', 'logistic', 'tanh', 'relu' default 'relu'
# max_iter=200
# alpha : default 0.0001 L2 penalty.

reg = MLPRegressor(hidden_layer_sizes = (100), solver = 'lbfgs')
reg.fit(x_train, y_train)

print 'R^2:', reg.score(x_test, y_test)

x_fine = np.linspace(0, 1, 1000).reshape(1000, 1) #sklearn works with transposed vectors

plt.scatter(x_test, y_test)
plt.plot(x_fine, reg.predict(x_fine), c='r')
plt.title('Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0.,1.])
plt.ylim([0.,2])
plt.savefig("3_Quadratic.png")
plt.show()