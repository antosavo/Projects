import numpy as np
import pandas as pd

s2 = pd.Series([5,-3,np.NaN,14])

print "\nSeries s2:\n", s2

print "\nNan valuse:\n", s2.isnull()

print "\nNan valuse Series:\n", s2[s2.isnull()]

print "\nNot Nan valuse:\n", s2.notnull()

print "\nNot Nan valuse Series:\n", s2[s2.notnull()]
