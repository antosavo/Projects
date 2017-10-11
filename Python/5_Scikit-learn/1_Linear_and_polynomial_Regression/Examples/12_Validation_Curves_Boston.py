'''
Validation curves are plots of the training and test accuracies as functions
of model parameters, for example, the inverse regularization parameter C in logistic regression.
'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.linear_model import Ridge
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import validation_curve
from sklearn.utils import shuffle

df = pd.read_excel('Boston.xls')

print 'Some Data:\n', df.head()
print 'Shape:', df.shape
#print 'Column Names:', df.columns.values
#print 'Correlation with MEDV:\n', df.corr()['MEDV'].abs().sort_values(ascending=False)

colnames = df.columns.values
features = colnames[:13]
target = colnames[13]

df = shuffle(df)
#df = df.sample(frac=1)

x = df[features]
y = df[target]

estimator = Ridge()

param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
#param_range = [0.00001, 0.0001, 0.001, 0.01]

train_scores, test_scores = validation_curve(estimator, x, y, cv=10, param_name='alpha', param_range= param_range ,n_jobs=-1)

train_scores_mean = np.mean(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)

plt.plot(param_range, train_scores_mean, 'o-', color="r",label="Training score")
plt.plot(param_range, test_scores_mean, 'o-', color="g",label="Test score")

plt.xlabel("alpha")
plt.xscale('log')
plt.ylabel("Score")
plt.ylim([0.1,1.01])
plt.legend(loc="best")

plt.savefig('12_Validation_Curves_Boston.png')
plt.show()