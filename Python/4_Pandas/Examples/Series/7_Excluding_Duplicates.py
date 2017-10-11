import numpy as np
import pandas as pd

sred = pd.Series([1,0,2,1,2,3], index=['white','white','blue','green','green','yellow'])

print "\nSeries sred:\n", sred

print "\nSeries no duplicates:", sred.unique()

print "\nSeries (value,counts):\n", sred.value_counts() 

print "\nValuse 0,3 ibn sred ?\n", sred.isin([0,3])

print "\nSeries with valuse 0,3:\n",  sred[sred.isin([0,3])]


