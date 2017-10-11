import numpy as np
import pandas as pd

frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
	index=['red','blue','yellow','white'],
	columns=['ball','pen','pencil','paper'])

frame2 = pd.DataFrame([[1,4,3,6],[4,5,6,1],[3,3,1,5],[4,1,6,4]],
	index=['red','blue','yellow','white'],
	columns=['ball','pen','pencil','paper'])

print "\nframe 2 :\n", frame2

print "\nframe 2 correlation:\n", frame2.corr()# ~ sum((x_i-<x>)*(y_i-<y>))

print "\nframe2 and 1 correlation:\n", frame2.corrwith(frame1)

