import pandas as pd
import numpy as np
import pylab as plt

frame1 = pd.DataFrame(np.random.rand(9).reshape(3,3), index=[1,2,3],
	columns=['A','B','C'])
print "\nframe1:\n", frame1

frame2 = pd.DataFrame(np.random.rand(3,3), index=[4,5,6],
	columns=['A','B','C'])
print "\nframe2:\n", frame2

print "\nconcat frame 1 and 2 axis 0:\n", pd.concat([frame1, frame2])

print "\nconcat frame 1 and 2 axis 1:\n", pd.concat([frame1, frame2],axis=1)





