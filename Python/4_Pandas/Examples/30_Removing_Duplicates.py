import numpy as np
import pandas as pd
import pylab as plt

dframe = pd.DataFrame({ 'color': ['white','white','red','red','white'],
	'value': [2,1,3,3,2]})
print "dframe:\n", dframe

print "duplicated ?\n", dframe.duplicated()

print "duplicates frame:\n", dframe[dframe.duplicated()]

print "no duplicates frame:\n", dframe.drop_duplicates() 


