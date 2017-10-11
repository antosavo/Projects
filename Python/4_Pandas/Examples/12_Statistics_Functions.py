import numpy as np
import pandas as pd

#frame = pd.DataFrame(np.arange(16).reshape((4,4)),
#	index=['red','blue','yellow','white'],
#	columns=['ball','pen','pencil','paper'])
frame = pd.DataFrame(np.random.rand(4,4),
	index=['red','blue','yellow','white'],
	columns=['ball','pen','pencil','paper'])

print "\nframe:\n", frame

print "\nframe['ball'] describe:\n", frame.loc[:,'ball'].describe()

print "\nframe['ball'] count:", frame.loc[:,'ball'].count()

print "\nframe['ball'] mean:", frame.loc[:,'ball'].mean()

print "\nframe['ball'] std:", frame.loc[:,'ball'].std()

print "\nframe['ball'] min:", frame.loc[:,'ball'].min()

print "\nframe['ball'] max:", frame.loc[:,'ball'].max()

print "\nframe['ball'] sum:", frame.loc[:,'ball'].sum()

print "\nframe correlation:\n", frame.corr()

print "\nframe covariance:\n", frame.cov()

print "\nframe['ball'] correlation frame['pen']:", frame['ball'].corr(frame['pen']) 

print "\nframe['ball'] covariance frame['pen']:", frame['ball'].cov(frame['pen']) 
