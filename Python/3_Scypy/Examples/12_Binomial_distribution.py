#binomial distribution is used to determine the probability of binary occurrences.
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
#import pylab as plt

x = np.linspace(0,10,11)

print x

n = 10
p = 0.5

g = binom(n, p) 
#n is the number of times the coin is flipped, p is the probability of success

print 'mean = ', g.mean()
print 'var = ', g.var()
print 'std = ', g.std()
print 'stats = ', g.stats()
print 'interval that contains 0.68 percent of the distribution = ', g.interval(0.68)
print '5 random values = ', g.rvs(5) #Random values


pmf = g.pmf(x)  #Probability mass function.
cdf = g.cdf(x)
ppf = g.ppf(x) #Percent point function inverse of cdf 


plt.plot(x, pmf, label ='pmf', color = 'blue')
plt.plot(x, cdf, label ='cdf', color = 'red')
plt.plot(x, ppf, label ='ppf', color = 'green')
plt.hist(g.rvs(1000), bins = 10,  normed = 1, label ='random rvs', color = "orange")
plt.ylim([0,2])
plt.legend(loc="upper left")
plt.show()


