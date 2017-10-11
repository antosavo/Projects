import numpy as np
import pandas as pd 

data = {'color' : ['blue','green','yellow','red','white'],
	'object' : ['ball','pen','pencil','paper','mug'],
	'price' : [1.2,1.0,0.6,0.9,1.7]}

frame = pd.DataFrame(data)

print "\nData Frame :\n", frame

frame.index.name = 'id' #assign name index
frame.columns.name = 'item' #assign name columns

print "\nData Frame new collective names index and column:\n", frame

frame.columns = ['color_1','object_1', 'price_1']
frame.index = ['A','B', 'C','D','E']

print "\nData Frame new names single index and column:\n", frame

print "\nData Frame change 1 row and one column:\n", frame.rename(index={'A':'alpha'}, columns={'object_1':'new_object'})
