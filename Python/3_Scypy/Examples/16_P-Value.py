#A p-value is the probability of rejecting a null-hypothesis when the hypothesis is
#proven true. The null hypothesis is a statement that says that there is no difference
#between two measures.
#Let's understand this concept with an example where the null hypothesis is that it is
#common for students to score 68 marks in mathematics.
#Let's define the significance level at 10%. If the p-value is less than 5%, then the null
#hypothesis is rejected and it is not common to score 68 marks in mathematics.
from scipy.stats import norm
from scipy.stats import zscore
import numpy as np
import matplotlib.pyplot as plt
#import pylab as plt

data = norm(50, 10).rvs(100).round()

zscore = ( 68 - data.mean() ) / data.std()

print 'z=', zscore 

p = 1 - norm.cdf(zscore)
p2 = 1 - norm(data.mean(),data.std()).cdf(68)
print 'Probability of getting a score higher than 68 =', p
print 'Probability of getting a score higher than 68 =', p2

#So, you can see that the p-value is at 5%, which is lower than the significance level.
#This means that the null hypothesis can be rejected, and it can be said that it's not
#common to get 68 marks in mathematics.






