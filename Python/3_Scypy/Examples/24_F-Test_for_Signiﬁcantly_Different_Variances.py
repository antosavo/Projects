#Bartlett's test tests the null hypothesis that all
#input samples are from populations with equal variances. 
import numpy as np
from scipy.stats import norm, bartlett

x1 = norm(0,3).rvs(10000)
x2 = norm(0,3).rvs(10000)

t = bartlett(x1, x2)

print 'The test statistic = ', t[0]
print 'p-value = ', t[1]