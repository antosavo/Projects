import numpy as np
import pandas as pd 

data = {'color' : ['blue','green','yellow','red','white'],
	'object' : ['ball','pen','pencil','paper','mug'],
	'price' : [1.2,1.0,0.6,0.9,1.7]}

frame = pd.DataFrame(data)
print "\nData Frame :\n", frame

frame['new'] = np.arange(5) #Update 'new'
print "\nData Frame :\n", frame

del frame['new'] #To delete new
print "\nDelete column 'new':\n", frame

print "\nDrop column color:\n", frame.drop('color',axis=1)

print "\nDrop row 0:\n", frame.drop(0)
