import pandas as pd
import numpy as np

s = pd.Series([12,-4,7,9], index=['a','b','c','d']) #assigned index

print "\nSeries s:\n", s

s[1] = 0

print "\nSeries s for s[1] = 0:\n", s




