import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
	index=['red','blue','yellow','white'],
	columns=['ball','pen','pencil','paper'])

print "\nDF:\n", frame

print "\nDF drop rows blue, yellow:\n", frame.drop(['blue','yellow'])

print "\nDF drop columns pen, pencil:\n", frame.drop(['pen','pencil'],axis=1)
