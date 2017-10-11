#A z-score is a score that expresses the value of a distribution in
#standard deviation with respect to the mean.
#z = (x-<x>)/sigma
from scipy.stats import norm
from scipy.stats import zscore
import numpy as np
import matplotlib.pyplot as plt

data = norm(50, 10).rvs(100).round()
#print data
#data = np.random.normal(50, 10, 100).round()
#50 is given as the mean of the distribution, 
#10 is the standard deviation of the distribution
#100 is the number of values to be generated

plt.hist(data, 30, normed=True) #Number of breaks is 30
plt.show()

z = zscore(data)
print z

mu = data.mean()
print 'mu=', mu
#print 'mu=', np.mean(data)

sigma = data.std()
print 'sigma=', sigma
#print 'sigma=', np.std(data)

z = (60-mu)/sigma
print 'z=', z 

print 'Probability of getting a score above (higher than) 60 =', 1 - norm.cdf(z)
print 'Probability of getting a score above (higher than) 60 =', 1 - norm(mu,sigma).cdf(60)
print 'ppf(cdf(z)) (percent point function inverse of cdf)=', norm.ppf(norm.cdf(z))






