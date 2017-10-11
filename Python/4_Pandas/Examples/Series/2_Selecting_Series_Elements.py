import pandas as pd
import numpy as np

s = pd.Series([12,-4,7,9], index=['a','b','c','d']) #assigned index

print "\nSeries s:\n", s

print "\ns['b'] = ", s['b']

print "\ns[1] = ", s[1]

print "\ns[0:2]:\n", s[0:2]

print "\ns[['a','b']]:\n", s[['a','b']]

