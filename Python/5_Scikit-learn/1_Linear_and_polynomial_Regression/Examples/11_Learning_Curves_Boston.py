'''
Learning curves are plots of the training and test accuracies as functions
of the sample size.
'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import learning_curve
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

estimator = LinearRegression()

train_sizes, train_scores, test_scores = learning_curve(estimator, x, y, cv=10, train_sizes=np.linspace(.1, 1.0, 5), n_jobs=-1)

train_scores_mean = np.mean(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)

plt.plot(train_sizes, train_scores_mean, 'o-', color="r",label="Training score")
plt.plot(train_sizes, test_scores_mean, 'o-', color="g",label="Test score")

plt.xlabel("Sample Size")
plt.ylabel("Score")
plt.ylim([0.1,1.01])
plt.legend(loc="best")

plt.savefig('11_Learning_Curves_Boston.png')
plt.show()