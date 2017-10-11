import numpy as np
import pandas as pd

mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
myseries = pd.Series(mydict)

print "\nmy series 1:\n",myseries

mydict2 = {'red':400,'yellow':1000,'black':700}
myseries2 = pd.Series(mydict2)

print "\nmy series 2:\n",myseries2

myseries3 =  myseries + myseries2

print "\nmy series 1 + 2 :\n",myseries3





