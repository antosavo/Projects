import pylab as plt
import pandas as pd
import numpy as np

colors = ['b','c','g','r']


for i in range(0,4):
  Pr = 150 + i*50
  df1 =pd.read_csv('Z-N-NLSE-P%d.dat'%Pr, header=None, sep='\t')
  df2 =pd.read_csv('Z-N-CM-P%d.dat'%Pr, header=None, sep='\t')
  df = pd.merge(df1,df2, on = 0)
  #df = df[(df['1_x']>0) & (df['1_y']>0) ]
  df = df[ df[0]> 100 ]
  z = df[0]
  N = (df['1_x']*5102041)/(df['1_y']*481184)
  plt.plot(z,N,c=colors[i],label='$P_{min}$=%d W'%Pr)

plt.legend(loc="lower right",frameon=False)
plt.xlabel('z [m]')
plt.xlim([150,500])
plt.ylabel('$N_{NLSE}\Delta T_{CM}/N_{CM}\Delta T_{NLSE}$')
plt.savefig('Number_events_Ratio.png')
plt.show()
