import numpy as np
import pandas as pd
import pylab as plt

N = 30
z = 100
Pr = 150

data = pd.DataFrame(np.zeros(2*3998).reshape((3998,2)))

for i in range(1,N+1):
  table = pd.read_table('seed_%d/TS_z_%d_Pr_%d.dat'%(i,z,Pr), header=None)
  data[1] += table[1]/N  
  
data[0] = table[0]

data.to_csv('TS_z_%d_Pr_%d.dat'%(z,Pr), sep='\t', header=None, index = None)

plt.plot(data[0],data[1])
plt.show()


##table = pd.read_table('seed_1/TS_z_100_Pr_150.dat', sep='\t', header=None)
#print "table idx<=10:\n", table[table.index <=10]
#print "table shape:\n", table.shape
#print "table describe:\n", table.describe()
#print "table columns:\n", table.columns
#print "table index:\n", table.index
#print "table[0] idx<=10:\n", table[table.index <=10][0]