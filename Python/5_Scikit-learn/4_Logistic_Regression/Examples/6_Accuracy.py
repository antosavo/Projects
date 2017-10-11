from sklearn.metrics import accuracy_score

y_true = [1, 1, 1, 1]
y_pred = [0, 1, 1, 0]

#Accuracy measures a fraction of the classifier's predictions that are correct.
print 'Accuracy:', accuracy_score(y_true, y_pred)
