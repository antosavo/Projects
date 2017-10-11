#A Poisson distribution is the probability distribution of independent events
#occurrences in an interval. 
#What would be the probability of n cars passing through the bridge in an hour?
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
#import pylab as plt

x = np.linspace(0,10,11)

print x

l = 2

g = poisson(l) 
#l is the mean number of occurrences.

print 'mean = ', g.mean()
print 'var = ', g.var()
print 'std = ', g.std()
print 'stats = ', g.stats()
print 'interval that contains 0.68 percent of the distribution = ', g.interval(0.68)
print '5 random values = ', g.rvs(5) #Random values


pmf = g.pmf(x)  #Probability mass function. x is the number of occurrences.
cdf = g.cdf(x)
ppf = g.ppf(x) #Percent point function inverse of cdf 


plt.plot(x, pmf, label ='pmf', color = 'blue')
plt.plot(x, cdf, label ='cdf', color = 'red')
plt.plot(x, ppf, label ='ppf', color = 'green')
plt.hist(g.rvs(1000), bins = 10,  normed = 1, label ='random rvs', color = "orange")
plt.ylim([0,2])
plt.legend(loc="upper right")
plt.show()


