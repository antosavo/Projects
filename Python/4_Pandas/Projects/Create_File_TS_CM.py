import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Pr = 150

for i in range(0,8):
  z = 150 + i*50 # i 0 to 15
  df = pd.read_csv('TS_z_%d_Pr_%d.dat'%(z,Pr), sep ='\t', header=None)
  df['t'] = df[0]
  df['a'] = df[1]/df[2]
  df.loc[:,['t','a']].to_csv('TS-CM_z_%d_P_%d.dat'%(z,Pr), sep = '\t', index=None, header=None)
