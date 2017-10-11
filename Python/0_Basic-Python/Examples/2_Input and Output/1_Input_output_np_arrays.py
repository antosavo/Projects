import numpy as np

data_in = np.loadtxt("Input_1.dat")
x = data_in[:,0]
y = data_in[:,1]

print x, type(x)
print y, type(y)

data_out = np.array([x,y]).T

np.savetxt("Output_1.dat",data_out,fmt="%lf") # It can print just numpy array

#np.savetxt("output_1.dat",data_out.T,fmt="%lf", delimiter = "\t", newline = "\n") # It can print just numpy array


