from scipy.stats import norm, relfreq
import numpy as np
import matplotlib.pyplot as plt
#import pylab as plt

x = norm().rvs(10)

print x

h = relfreq(x, numbins=4, defaultreallimits = [-3,3])

print 'Relfreq:', h
print 'Frequency:', h[0]
print 'Lowerlimit:', h[1]
print 'Binsize:', h[2]
print 'Extrapoints:', h[3]
print 'Frequency sum:', h[0].sum()


