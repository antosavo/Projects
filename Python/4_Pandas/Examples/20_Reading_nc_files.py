import pylab as plt
import pandas as pd
import numpy as np
import netCDF4

Pr = 150

nc = netCDF4.Dataset('mo_150.nc')

print 'variables:\n', nc.variables

z = nc.variables['z']
t = nc.variables['t']
u = nc.variables['P']

for i in range(0,7):
  k=100-i*10
  plt.scatter(-t[:], u[k,:]/10000.0, cmap = "jet", c=z[k]*1000*np.ones(4095), marker='o', edgecolor = "none", vmin = 200, vmax = 500)

cbar = plt.colorbar()
cbar.set_label("z [m]",fontsize=18)
cbar.set_ticks([200,250,300,350,400,450,500])
cbar.ax.tick_params(labelsize=16)

plt.text(0.5,0.1,"$\mathrm{P_{min} = %i W}$"%Pr,fontsize=18)
plt.tick_params(labelsize=18)
plt.xlabel('$\Delta t$ [ps]',fontsize=18)
plt.ylabel('$|u(\Delta t)|^2$/$\left<|u(\Delta t)|^2\\right>$',fontsize=18)
plt.xlim([-2.5,2.5])
plt.xticks([-2,-1,0,1,2])
plt.ylim([0,1.1])
plt.savefig("TS_2D_Pr_%i.eps"%Pr)
plt.show()
