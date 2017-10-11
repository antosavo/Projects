#The conventional statistic for measuring the significance 
#of a difference of means is termed Student's t. 
#Test if the means of two random variables are equal.

import numpy as np
from scipy.stats import norm, ttest_ind

x1 = norm(0,3).rvs(1000000)
x2 = norm(0,4).rvs(1000000)

t = ttest_ind(x1, x2, equal_var= False)

print 't statistic = ', t[0]
print 'p-value = ', t[1]