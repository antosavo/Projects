import numpy as np
import pandas as pd
#import pylab as plt
import matplotlib.pyplot as plt

z = 1500
data = pd.read_csv('PI_PF_z_%d.dat'%z, sep ='\t', header = None)
#print data

colors = ['blue','red']

data_b = data[data[0]<=45]
data_r = data[data[0]>45]

plt.scatter(data_b[0], data_b[1], color = colors[0] , marker = "s", edgecolor = "none")
plt.scatter(data_r[0], data_r[1], color = colors[1] , marker = "s", edgecolor = "none" )
#plt.plot([45,45],[0,1500], linewidth=2.0, color='black')
plt.title('z = %d m'%z)
plt.xlim([0,100])
plt.xlabel('$P_I$ [W]')
plt.ylim([0,1500])
plt.ylabel('$P_F$')
plt.savefig('PI_PF_%d_B.png'%z)
plt.show()