import numpy as np
import pandas as pd

frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
	index=['red','blue','yellow','white'],
	columns=['ball','pen','pencil','paper'])

print "\nframe1:\n", frame1

frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
	index=['blue','green','white','yellow'],
	columns=['mug','pen','ball'])

print "\nframe2:\n", frame2

print "\nframe1+frame2:\n", frame1.add(frame2)

print "\nframe1-frame2:\n", frame1.sub(frame2)

print "\nframe1/frame2:\n", frame1.div(frame2)

print "\nframe1*frame2:\n", frame1.mul(frame2)

