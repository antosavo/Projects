import pandas as pd
import numpy as np

s0 = pd.Series([12,-4,7,9]) #default index from 0

print "\nSeries s0:\n", s0

s = pd.Series([12,-4,7,9], index=['a','b','c','d']) #assigned index

print "\nSeries s:\n", s

print "\ns.index = ", list(s.index)

print "\ns.values = ", s.values

