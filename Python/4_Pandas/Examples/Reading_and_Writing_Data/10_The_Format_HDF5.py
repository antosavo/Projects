#The HDF term stands for Hierarchical Data Format.
import numpy as np
import pandas as pd
from pandas.io.pytables import HDFStore

store = HDFStore('mydata.h5')

frame = pd.DataFrame(np.arange(16).reshape(4,4),
	index=['white','black','red','blue'],
	columns=['up','down','right','left'])

store['obj1'] = frame

#you can store multiple data structures within a single file
frame2 = pd.DataFrame(np.random.random((4,4)),
	index=['white','black','red','blue'],
	columns=['up','down','right','left'])

store['obj2'] = frame2

print "store:\n", store

print "store[1]:\n", store['obj1']

print "store[2]:\n", store['obj2']

