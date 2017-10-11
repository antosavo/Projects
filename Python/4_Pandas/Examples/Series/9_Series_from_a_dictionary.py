import numpy as np
import pandas as pd

mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}

print "my dictionary:\n",mydict

myseries = pd.Series(mydict)

print "my series:\n",myseries

colors = ['red','yellow','orange','blue','green']
myseries = pd.Series(mydict, index=colors)

print "my series 2:\n",myseries

