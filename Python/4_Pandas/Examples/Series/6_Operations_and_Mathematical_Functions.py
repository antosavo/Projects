import pandas as pd
import numpy as np

s = pd.Series([12,-4,7,9], index=['a','b','c','d']) #assigned index

print "\nSeries s:\n", s

print "\nSeries s/2:\n", s/2

print "\nSeries log(s):\n", np.log(s)





