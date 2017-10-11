import numpy as np
import pandas as pd

#hierarchical DF
mframe = pd.DataFrame(np.random.randn(16).reshape(4,4),
	index=[['white','white','red','red'], ['up','down','up','down']],
	columns=[['pen','pen','paper','paper'],['A','B','A','B']])
print "\nDF:\n", mframe

mframe.columns.names = ['objects','id']
mframe.index.names = ['colors','status']
print "\nDF plus names:\n", mframe

print "\nDF swapped names:\n", mframe.swaplevel('colors','status')

print "\nDF sortlevel colors:\n", mframe.sortlevel('colors')

print "\nsum colors:\n", mframe.sum(level='colors')

print "\nsum id:\n", mframe.sum(level='id',axis=1)

