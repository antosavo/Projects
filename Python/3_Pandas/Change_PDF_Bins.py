import numpy as np
import pandas as pd
import pylab as plt

data = pd.read_csv('PDF_500.dat', sep='\t', header=None)

#N = int(data.shape[0]/2.5)
N = 400 
 
new_data = pd.DataFrame(np.zeros(2*N).reshape((N,2)))

for i in range (0, N):
  new_data.loc[i,0] = (i+1)*2.5
  new_data.loc[i,1] = data[(data[0]>i*2.5) & (data[0]<=(i+1)*2.5)][1].sum()

new_data[1] = new_data[1]/(2.5*new_data[1].sum())

print new_data

new_data.to_csv('PDF_500_Bins_2_5.dat', sep = '\t', index=None, header=None)