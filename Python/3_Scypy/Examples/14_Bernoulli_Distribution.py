#You can perform an experiment with two possible outcomes: success or failure.
#Success has a probability of p, and failure has a probability of 1 - p. A random
#variable that takes a 1 value in case of a success and 0 in case of failure is called
#a Bernoulli distribution.
#Voting in an election is a good example of the Bernoulli distribution.

from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt
#import pylab as plt

x = np.linspace(0,10,11)

print x

p = 0.7

g = bernoulli(p) 
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
plt.hist(g.rvs(10000), bins = [-0.5,0.5,1.5],  normed = 1, label ='random rvs', color = "orange")
plt.xlim([-1,2])
plt.ylim([0,1.2])
plt.legend(loc="upper left")
plt.show()


