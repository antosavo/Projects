import numpy as np
import pandas as pd 

data = {'color' : ['blue','green','yellow','red','white'],
	'object' : ['ball','pen','pencil','paper','mug'],
	'price' : [1.2,1.0,0.6,0.9,1.7]}

frame = pd.DataFrame(data)
print "\nData Frame :\n", frame

print "\nIs in :\n", frame.isin([1.2,'pen'])

print "\nIs in :\n", frame[frame.isin([1.2,'pen'])]


