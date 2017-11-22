import numpy as np
import pylab as plt

Pr = 300

for i in range(0,13):
  #z = i*100
  z = 1500 - i*100 # i 0 to 15

  data = np.loadtxt("TS_z_%d_Pr_%d.dat"%(z,Pr))
  t = data[:,0]
  a = data[:,1]/data[:,2]
  Z = np.ones(len(t))*z
  plt.scatter(t, a, cmap = "jet", c =Z, marker='o', edgecolor = "none", vmin = 300, vmax = 1500)

cbar = plt.colorbar()
cbar.set_label("z [m]",fontsize=18)
#cbar.set_ticks([200,400,600,800,1000,1200,1400])
cbar.set_ticks([300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500])
cbar.ax.tick_params(labelsize=16)

#plt.title("Pr = %i"%Pr,fontsize=18)
#plt.text(0.5,0.003,"P$_{min}$ = %i W"%Pr,fontsize=18, style='normal')
plt.text(0.5,0.1,"$\mathrm{P_{min} = %i W}$"%Pr,fontsize=18)
#plt.tick_params(labelsize=16,width=1)
plt.tick_params(labelsize=18)
plt.xlabel('$\Delta t$ [ps]',fontsize=18)
plt.ylabel('$|u(\Delta t)|^2$/$\left<|u(\Delta t)|^2\\right>$',fontsize=18)
plt.xlim([-2,2])
plt.xticks([-2,-1,0,1,2])
plt.ylim([0,1])
plt.savefig("TS_2D_Pr_%i.eps"%Pr)
plt.show()
