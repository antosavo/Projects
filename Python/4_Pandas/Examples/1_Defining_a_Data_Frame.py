import numpy as np
import pandas as pd 

data = {'color' : ['blue','green','yellow','red','white'],
	'object' : ['ball','pen','pencil','paper','mug'],
	'price' : [1.2,1.0,0.6,0.9,1.7]}

frame1 = pd.DataFrame(data)

print "\nData Frame 1:\n", frame1

frame2 = pd.DataFrame(np.arange(16).reshape((4,4)),
	index=['red','blue','yellow','white'],
	columns=['ball','pen','pencil','paper'])

print "\nData Frame 2:\n", frame2

frame3 = pd.DataFrame([
	['green', 'M', 10.1, 'class1'],
	['red', 'L', 13.5, 'class2'],
	['blue', 'XL', 15.3, 'class1']])

frame3.columns = ['color', 'size', 'price', 'classlabel']

print "\nData Frame 3:\n", frame3




