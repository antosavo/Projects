import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

y = [0, 1, 1, 0] * 10000
x = [[0, 0], [0, 1], [1, 0], [1, 1]] * 10000

x_train, x_test, y_train, y_test = train_test_split(x, y)

# for 3 hidden_layer_sizes = (100,100,100) #default (100)
# solver : {'lbfgs','sgd', 'adam'}, default 'adam'
# learning_rate_init : double, default 0.001
# activation : 'identity', 'logistic', 'tanh', 'relu' default 'relu'
# max_iter=200
# alpha : default 0.0001 L2 penalty.

#clf = MLPClassifier(hidden_layer_sizes = (2), activation='logistic', solver='sgd', learning_rate_init=1)
clf = MLPClassifier(hidden_layer_sizes = (10), solver='lbfgs')
clf.fit(x_train, y_train)

print 'Number of layers:', clf.n_layers_
print 'Number of hidden layers:', clf.n_layers_ - 2
print 'Number of outputs:', clf.n_outputs_

print 'Accuracy:', clf.score(x_test, y_test)

y_pred = clf.predict(x_test)

table = pd.crosstab(np.array(y_test), y_pred, rownames=['Actual'], colnames=['Predictions'])
print table


