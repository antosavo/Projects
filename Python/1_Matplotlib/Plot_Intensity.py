''' Script to Plot and Fitt '''

import numpy as np
import matplotlib.pyplot as plt

color_x = ["blue","green","yellow","orange","red"]
label_x = ["0 m","250 m","500 m","750 m","1000 m"]

for j in range(0,5):

  k=j*250

  data = np.loadtxt("Intensity_12_%d.dat"%k)
  
  x = data[:,0]
  y = data[:,1]

#Plot

  #plt.clf() # Clear the figure
  #plt.title("Intensity",fontsize=16)
  plt.xlabel("$t$ [ps]",fontsize=16)
  plt.ylabel("$|u|^2$ [W]",fontsize=16)
  plt.xlim([-1,11])
  #plt.xticks([0,90,180,270,360],["$0$","$\\frac{1}{2}\\pi$","$\\pi$","$\\frac{3}{2}\\pi$","$2$$\\pi$"])
  plt.ylim([0.000001,110])
  #plt.yscale("log")
  #plt.yticks([-0.05,0.00,0.05,0.10,0.15,0.20,0.25],["-0.05","0.00","0.05","0.10","0.15","0.20","0.25"])
  plt.tick_params(labelsize=16,width=1)

  plt.plot(x, y, label = label_x[j],linestyle="-", linewidth=2.0, marker= "", markeredgecolor= color_x[j],markersize=5, color= color_x[j])
  plt.legend(numpoints=1,loc="upper right",frameon=False,fontsize=16)
  plt.tight_layout()

plt.savefig("Intensity_Linear.png")
plt.show()

