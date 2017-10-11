import numpy as np
import pandas as pd
import pylab as plt

randframe = pd.DataFrame(np.random.randn(1000,3)) # 1000x3 normal distributed
print "describe df:\n", randframe.describe()
print "std df:\n", randframe.std()

print "filtered values column 0:\n", randframe.loc[(np.abs(randframe[0]) > (3*randframe[0].std())),0]
print "filtered values:\n", randframe[(np.abs(randframe) > (3*randframe.std())).any(1)]


