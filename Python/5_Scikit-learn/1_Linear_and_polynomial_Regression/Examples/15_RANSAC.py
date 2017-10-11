'''
RANSAC algorithm fits a regression model just to the inliers data.
'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression, RANSACRegressor

df = pd.read_excel('Boston.xls')

x = df[['RM']]
y = df['MEDV']

ransac = RANSACRegressor(LinearRegression(),
  max_trials=100,
  min_samples=50)

ransac.fit(x, y)

inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)

x_fine = np.arange(3, 10, 1).reshape(-1,1)

y_fine = ransac.predict(x_fine)

plt.scatter(x[outlier_mask], y[outlier_mask], c='g', marker='s', label='Outliers')
plt.scatter(x[inlier_mask], y[inlier_mask], c='b', marker='o', label='Inliers')
plt.plot(x_fine, y_fine, c='r')

plt.xlabel('RM')
plt.ylabel('MEDV')
plt.legend(loc='upper left')
plt.show()