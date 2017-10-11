import math
import numpy as np
#import pylab as plt
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

mean = 100
sigma = 15
Number = 10000

x = np.random.normal(mean, sigma, Number)
x2 = np.arange(40,160,0.5)

plt.hist(x, bins = 50,  normed = 1, color = "green")
#plt.plot(x2, plt.normpdf(x2, mean, sigma), color = "blue")
plt.plot(x2, mlab.normpdf(x2, mean, sigma), color = "blue")
plt.xlabel("bins")
plt.ylabel("Probability")
plt.savefig("Histogram.png")
plt.show()