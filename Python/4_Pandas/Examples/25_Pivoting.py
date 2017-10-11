import numpy as np
import pandas as pd
import pylab as plt

#pivoting: converting columns to rows
frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
	index=['white','black','red'],
	columns=['ball','pen','pencil'])
print "frame1:\n", frame1

#stacking: rotates or pivots the data structure converting columns to rows
ser = frame1.stack()
print "stack frame1:\n", ser 

print "unstack frame1:\n", ser.unstack()
print "unstack frame1 level 0:\n", ser.unstack(0)

