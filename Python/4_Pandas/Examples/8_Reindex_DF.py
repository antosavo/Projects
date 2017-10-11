import numpy as np
import pandas as pd 

data = {'color' : ['blue','green','yellow','red','white'],
	'object' : ['ball','pen','pencil','paper','mug'],
	'price' : [1.2,1.0,0.6,0.9,1.7]}

frame = pd.DataFrame(data)
print "\nData Frame:\n", frame

frame2 = frame.reindex([4,3,2,1,0,5],fill_value='missing')
print "\nReindex Data Frame:\n", frame2





