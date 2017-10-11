import numpy as np

x,y = np.loadtxt("Input_2.dat")

print x, type(x)
print y, type(y)

np.savetxt("Output_2.dat",[x,y],fmt="%lf", newline = "\t") # It can print just numpy array
