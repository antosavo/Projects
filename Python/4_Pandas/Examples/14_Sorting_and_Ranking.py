import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
	index=['red','blue','yellow','white'],
	columns=['ball','pen','pencil','paper'])
print "\nframe:\n", frame

print "\nsorted rows frame (a-z):\n", frame.sort_index()

print "\nsorted rows frame (z-a):\n", frame.sort_index(ascending=False)

print "\nsorted columns frame:\n", frame.sort_index(axis=1)

print "\nsorted by column pen:\n", frame.sort_index(by='pen')

print "\nsorted by column pen and pencil:\n", frame.sort_index(by=['pen','pencil'])

print "\nsorted by column pen 2:\n", frame.sort('pen', ascending=False)

print "\nordered pen:\n", frame['pen'].order()




