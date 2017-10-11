import math
import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
	index=['red','blue','yellow','white'],
	columns=['ball','pen','pencil','paper'])

def F(x):
  return (x+1)**2

print "\nframe:\n", frame

print "\nsqrt(frame):\n", np.sqrt(frame)

print "\nframe apply F(x):\n", frame.apply(F)

print "\nsqrt(frame.loc['red','ball']):\n", np.sqrt(frame.loc['red','ball'])

print "\nsqrt(frame.loc[:,'ball']):\n", np.sqrt(frame.loc[:,'ball'])

print "\nsqrt(frame.loc[['red','yellow'],['ball','pen']]):\n", np.sqrt(frame.loc[['red','yellow'],['ball','pen']])




