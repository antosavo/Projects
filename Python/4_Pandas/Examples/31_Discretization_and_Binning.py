import numpy as np
import pandas as pd
import pylab as plt

x = pd.Series([12,34,67,55,28,90,99,12,3,56,74,44,87,23,49,89,87])

h = np.histogram(x, bins=4, range=[0,100], normed=True)

print "Histogram Numpy:\n", h
print "PDF h[0]:", h[0]
print "Intervals h[1]:", h[1]
print "PDF sum:", h[0].sum() 

plt.hist(x, bins = 4, normed = 1, color = "green")
plt.show()





