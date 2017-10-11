import numpy as np
import pandas as pd
import pylab as plt

#Adding Values via Mapping
frame2 = pd.DataFrame({ 'item':['ball','mug','pen','pencil','ashtray'],
		        'color':['white','red','green','black','yellow']})
print "frame2:\n", frame2

prices = {
  'ball' : 5.56,
  'mug' : 4.20,
  'bottle' : 1.30,
  'scissors' : 3.41,
  'pen' : 1.30,
  'pencil' : 0.56,
  'ashtray' : 2.75
  }

frame2['price'] = frame2['item'].map(prices)
print "frame2:\n", frame2

#Rename the Indexes of the Axes
reindex = {
  0: 'first',
  1: 'second',
  2: 'third',
  3: 'fourth',
  4: 'fifth'
  }
print "frame2 reindex:\n", frame2.rename(reindex)

recolumn = {'item':'object','price': 'value'}
print "frame2 reindex and recolumn:\n", frame2.rename(index=reindex, columns=recolumn)

print "frame2 change 1 row and one column:\n", frame2.rename(index={1:'first'}, columns={'item':'object'})

#The rename() function returns a DataFrame with the changes, leaving
#unchanged the original DataFrame. If you want the changes to take effect on the object on which you call the
#function, you will set the inplace option to True.
frame2.rename(columns={'item':'object'}, inplace=True)
print "frame2 changed permanently:\n", frame2
















