import numpy as np
import pandas as pd
import pylab as plt

#Replace
frame = pd.DataFrame({ 'item':['ball','mug','pen','pencil','ashtray'],
		       'color':['white','rosso','verde','black','yellow'],
		       'price':[5.56,np.nan,1.30,np.nan,2.75]})
print "frame:\n", frame

print "frame without nan:\n", frame.replace(np.nan,0)

#Replacing Values via Mapping
newcolors = {'rosso': 'red','verde': 'green'}
print "frame newcolors:\n", frame.replace(newcolors)
















