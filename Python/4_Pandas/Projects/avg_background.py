import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import relfreq

df = pd.read_csv( 'Intensity_1500.dat', sep='\t', header=None)

I = df[1]
#print I
x = []

b = 0.0
vb = 0.0
n = 0.0
Nb = 60


for i in range(0,df.shape[0]-2):
  if I[i+1]< I[i] and I[i+1]< I[i+2]:
    n += 1
    b += I[i+1]
    x.append(I[i+1])

I_b = b/n

for i in range(0,df.shape[0]-2):
  if I[i+1]< I[i] and I[i+1]< I[i+2]:
    vb += ((I[i+1]-I_b)**2)/(n-1)

print 'avg background = ', I_b
print 'std background = ', np.sqrt(vb)

h = relfreq(x, numbins=Nb, defaultreallimits = [0,60])

print 'Frequency:', h[0]
print 'Lowerlimit:', h[1]
print 'Binsize:', h[2]
print 'Extrapoints:', h[3]
print 'Frequency sum:', h[0].sum()

plt.plot(np.linspace(60/(2.0*Nb),60,Nb),h[0])
plt.xlim([0,20])
plt.xlabel('P')
plt.ylim([0,1])
plt.ylabel('Frequency')
plt.savefig('Frequency_min.png')
plt.show()

df_out = pd.DataFrame({0 : np.linspace(60/(2.0*Nb),60,Nb), 1 : h[0]}).to_csv('Frequency.dat', sep = '\t', index=None, header=None)