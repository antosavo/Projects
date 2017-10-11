import numpy as np
import pandas as pd
import pylab as plt

longframe = pd.DataFrame({ 'color':['white','white','white',
	'red','red','red',
	'black','black','black'],
'item':['ball','pen','mug',
	'ball','pen','mug',
	'ball','pen','mug'],
'value': np.random.rand(9)})

print "longframe:\n", longframe

#pivot() makes a transformation of a DataFrame
#from the long type to the wide type.  
wideframe = longframe.pivot('color','item')
print "wideframe:\n", wideframe


