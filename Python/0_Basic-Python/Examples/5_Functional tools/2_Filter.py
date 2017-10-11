import numpy as np

def greater_than_5(x):
  if x>5:
    return True
  else:
    return False

f_11 = filter(greater_than_5,range(11))

print f_11, "\n", type(f_11)

np.savetxt("Output_2.dat",f_11,fmt="%lf")