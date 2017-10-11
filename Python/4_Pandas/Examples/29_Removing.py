import numpy as np
import pandas as pd
import pylab as plt

frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
	index=['white','black','red'],
	columns=['ball','pen','pencil'])
print "frame1:\n", frame1

#removing column 
del frame1['ball']
print "frame1 del column ball:\n", frame1

#removing row
print "frame1 drop row white:\n", frame1.drop('white')