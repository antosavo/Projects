#The Chi-square test can be used to test whether the observed data differs
#significantly from the expected data.
import numpy as np
from scipy.stats import chisquare

expected = np.array([6,6,6,6,6,6])

observed = np.array([7, 5, 3, 9, 6, 6])

chi_2 = chisquare(observed, expected)#sum((Oi - Ei)^2/Ei)

print "chisquare=", chi_2[0]
print "p-value=", chi_2[1]

#The first value is the chi-square value and the second value is the p-value, which
#is very high. This means that the null hypothesis is valid and the observed value is
#similar to the expected value.

