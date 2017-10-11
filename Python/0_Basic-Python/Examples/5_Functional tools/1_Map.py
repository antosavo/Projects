import numpy as np

def f(x):
  return x**2

f_10 = map(f,range(10))

print f_10, "\n", type(f_10)

np.savetxt("Output_1.dat",f_10,fmt="%lf")