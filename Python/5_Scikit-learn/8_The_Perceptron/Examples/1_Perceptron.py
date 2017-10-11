#Perceptrons are capable of online, error-driven learning;
#the learning algorithm can update the model's parameters using a single training
#instance rather than the entire batch of training instances. Online learning is useful
#for learning from training sets that are too large to be represented in memory.
#The perceptron learning algorithm begins by setting the weights to small
#random values. It then predicts the class for a training instance. The perceptron is an
#error-driven learning algorithm; if the prediction is correct, the algorithm continues
#to the next instance. If the prediction is incorrect, the algorithm updates the weights.
#This update rule is similar to the update rule for gradient descent.
#Linear models like the perceptron with a Heaviside activation function
#are not universal function approximators; they cannot represent some functions.
#Specifically, linear models can only learn to approximate the functions for linearly
#separable datasets. The linear classifiers that we have examined find a hyperplane
#that separates the positive classes from the negative classes; if no hyperplane exists
#that can separate the classes, the problem is not linearly separable.
#A simple example of a function that is linearly inseparable is the logical operation
#XOR, or exclusive disjunction.
import numpy as np
import pandas as pd
import pylab as plt
from sklearn.linear_model import Perceptron


X = np.array([
    [0.2, 0.1],
    [0.4, 0.6],
    [0.5, 0.2],
    [0.7, 0.9]])

y = [0, 0, 0, 1]

classifier = Perceptron(n_iter=100, eta0=0.5) #eta0: Constant by which the updates are multiplied. Defaults to 1.
classifier.fit(X, y)

print 'intercept= ', classifier.intercept_[0]
print 'weights= ', classifier.coef_[0] 
print 'predictions:\n', classifier.predict(X)

#b + w1*x1 + w2*x2 = 0 => x2 = -( b + w1*x1 )/w2
b = classifier.intercept_[0] 
w = classifier.coef_[0]
x_l = np.linspace(0,1,10)
y_l = -(b + w[0]*x_l)/w[1]


plt.scatter(X[:3, 0], X[:3, 1], marker='.', s=400)
plt.scatter(X[3, 0], X[3, 1], marker='x', s=400)
plt.plot(x_l, y_l, color='red')
plt.xlabel('x1')
plt.xlim([0,1])
plt.ylabel('x2')
plt.savefig('Perceptron.png')
plt.show()

