from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
#import pylab as plt

x = np.linspace(-2,2,20)

mean = 0.0
sigma = 0.5

g = norm( mean, sigma)

print 'mean = ', g.mean()
print 'var = ', g.var()
print 'std = ', g.std()
print 'stats = ', g.stats()
print 'interval that contains 0.68 percent of the distribution = ', g.interval(0.68)
print '5 random values = ', g.rvs(5) #Random values
print 'fit=', norm.fit(g.rvs(10000))

a, b = norm.fit(g.rvs(10000))

pdf = g.pdf(x)
cdf = g.cdf(x)
ppf = g.ppf(x) #Percent point function inverse of cdf 


plt.plot(x, pdf, label ='pdf', color = 'blue')
plt.plot(x, cdf, label ='cdf', color = 'red')
plt.plot(x, ppf, label ='ppf', color = 'green')
plt.hist(g.rvs(1000), bins = 10,  normed = 1, label ='random rvs', color = "orange")
plt.plot(x, norm(a,b).pdf(x), label ='fit', color = 'cyan')
plt.legend(loc="upper left")
plt.show()


