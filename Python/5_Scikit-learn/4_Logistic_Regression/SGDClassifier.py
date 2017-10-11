from sklearn.linear_model import SGDClassifier # stochastic gradient algorithm

ppn = SGDClassifier(loss='perceptron')
lr = SGDClassifier(loss='log')
svm = SGDClassifier(loss='hinge')

partial_fit #online learning
