#This tests whether 2 samples are drawn from the same distribution. 
#Note that the distribution is assumed to be continuous.
#Returns the KS statistic and two-tailed p-value
#If the K-S statistic is small or the p-value is high, then the distributions of the two samples are probably the same.
import numpy as np
from scipy.stats import norm, ks_2samp

x1 = norm(0,3).rvs(100000)
x2 = norm(0,3).rvs(100000)

ks = ks_2samp(x1, x2)

print 'KS statistic = ', ks[0]
print 'p-value = ', ks[1]