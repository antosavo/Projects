#The chi-square test of independence is a statistical test used to determine whether
#two categorical variables are independent of each other or not.
#The test for differences between binned distributions is the chi-square
#test. For continuous data as a function of a single variable, the used
#test is the Kolmogorov-Smirnov test.
#A large value of chi-square indicates that the null hypothesis 
#(that two data sets are drawn from the same pdf) is rather unlikely.
#If the data were collected in such a way that the sum of the NAi's is necessarily
#equal to the sum of NBi's, then the number of degrees of freedom is equal to the 
#number of bins less one. If this requirement were absent, then the number of 
#degrees of freedom would be number of bins.
import numpy as np
from scipy.stats import chi2_contingency, chisquare, chi2
from scipy.stats import norm, relfreq

N = 1000

x1 = norm(0,3).rvs(N)
x2 = norm(0,3).rvs(N)

h1 = relfreq(x1, numbins=11, defaultreallimits = [-6,6])
h2 = relfreq(x2, numbins=11, defaultreallimits = [-6,6])

x1_x2 = np.array([N*h1[0], N*h2[0]])

print "M=", x1_x2

chi_2 = chi2_contingency(x1_x2) #sum((NAi - NBi)^2/(NAi + NBi))

print "chi-square statistic = ", chi_2[0]
print "p-value = ", chi_2[1]
print "degrees of freedom = ", chi_2[2]
print "expected frequencies 1 = \n", chi_2[3][0] 
print "expected frequencies 2 = \n", chi_2[3][1]
#The first value is the chi-square value
#The second value is the p-value, which is very big, and means that 
#the two distributions are the same. 

#chi_2_B = np.sum(((h1[0]-h2[0])**2)/(h1[0]+h2[0]))
#print "\nchisquare B = ", chi_2_B
#print "p-value B = ", 1 - chi2.cdf(chi_2[0], chi_2[2])
