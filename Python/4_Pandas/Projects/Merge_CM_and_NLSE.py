import pylab as plt
import pandas as pd
import numpy as np

colors = ['b','c','g','r']


for i in range(0,4):
  Pr = 150 + i*50
  df1 =pd.read_csv('Z-N-NLSE-P%d.dat'%Pr, header=None, sep='\t')
  df2 =pd.read_csv('Z-N-CM-P%d.dat'%Pr, header=None, sep='\t')

  df = pd.merge(df1,df2, on = 0)

  df = df[ df[0]> 100 ]

  df.columns = ['z','N_NLSE','N_CM']
  df['N_NLSE_over_T']= df['N_NLSE']/481184
  df['N_CM_over_T']= df['N_CM']/5102041
  df['Ratio']= df['N_NLSE_over_T']/df['N_CM_over_T']
  
  df.loc[:,['z','N_NLSE_over_T']].to_csv('N_over_T_NLSE-P%d.dat'%Pr, sep = '\t', index=None, header=None)
  df.loc[:,['z','N_CM_over_T']].to_csv('N_over_T_CM-P%d.dat'%Pr, sep = '\t', index=None, header=None)
  df.loc[:,['z','Ratio']].to_csv('Ratio-P%d.dat'%Pr, sep = '\t', index=None, header=None)
  
