import numpy as np
import pandas as pd
#import pylab as plt
import matplotlib.pyplot as plt

for i in range(0,13):
  z = 300+i*100
  #z = 1500 - i*100 # i 0 to 15
  data = pd.read_csv('LR_z_%d.dat'%z, sep ='\t', header = None)
  Z = np.ones(len(data[0]))*z
  #dataf = data.dropna()
  dataf = data[data[1] != np.nan]
  plt.scatter(dataf[0], dataf[1], cmap = "jet", c =Z, marker='o', edgecolor = "none", vmin = 300, vmax = 1500)

cbar = plt.colorbar()
cbar.set_label("z [m]",fontsize=18)
cbar.set_ticks([300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500])
cbar.ax.tick_params(labelsize=16)

plt.xlim([0,160])
plt.xlabel('$P$ [W]')
plt.ylim([0,1.1])
plt.ylabel('Probability($P_F$ > $P_I$)')
plt.savefig('Lr_All.png')
plt.show()
