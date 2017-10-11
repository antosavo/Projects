import numpy as np
from scipy.stats import norm, f_oneway

x1 = norm(0,3).rvs(1000000)
x2 = norm(0,3).rvs(1000000)

F = f_oneway(x1, x2)

print 'F-value = ', F[0]
print 'p-value = ', F[1]