#In k-fold cross-validation, we randomly split the training dataset into k folds without
#replacement (each sample point will be part of a training and test dataset exactly once), 
#where k - 1 folds are used for the model training and one fold is used
#for testing. This procedure is repeated k times so that we obtain k models and
#performance estimates.
#We then calculate the average performance to obtain an estimate that is less sensitive to the
#subpartitioning.
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score, cross_val_predict

df = pd.read_csv('winequality-red.csv', sep=';')

Names = df.columns.values[0:-1]

x = df[Names]#the last column is the quality that is the y parameter, [0:-1] means all but not the last
y = df['quality']

model = LinearRegression()

scores = cross_val_score(model, x, y, cv=5, n_jobs=-1) #by default cross-validation cv =  3-fold
#n_jobs = N then N CPU will be used. By setting n_jobs=-1, we can use all available CPUs on our machine.

print "<R^2> = ", scores.mean(), "\nR^2 = ", scores

y_pred = cross_val_predict(model, x, y, cv=5)

print 'Some predictions:\n', y_pred



