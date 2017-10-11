import numpy as np
import pandas as pd 

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
	index=['red','blue','yellow','white'],
	columns=['ball','pen','pencil','paper'])

print "\nData Frame:\n", frame

print "\nDF shape:\n", frame.shape

print "\nDf columns:", frame.columns

print "\nDf columns values:", frame.columns.values

print "\nDf index(rows):", frame.index #cannot be changed

print "\nDf index(rows) values:", frame.index.values

print "\nDf values:\n", frame.values

print "\nelemet['red','pen']:", frame.loc['red','pen']

print "\nelemet['red','pen'] 2:", frame['pen']['red']

print "\nelemet[0,1]:", frame.iloc[0,1]

print "\ncolumn[pen]:\n", frame.loc[:,'pen']

print "\ncolumn[pen] 2:\n", frame['pen']

print "\ncolumns['ball','pen']:\n", frame.loc[:,['ball','pen']]

print "\nrow[red]:\n", frame.loc['red',:]

print "\nrow[red] 2:\n", frame.ix['red']

print "\nrows['red','yellow']:\n", frame.loc[['red','yellow'],:]

print "\nrows['red','yellow'] 2:\n", frame.take([0,2])

print "\nelemets[['red','yellow'],['ball','pen']]:\n", frame.loc[['red','yellow'],['ball','pen']]

print "\nframe = 2:\n", frame[frame==2]

print "\nframe > 2:\n", frame[frame>2]






