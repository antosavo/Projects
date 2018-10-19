import numpy as np
import matplotlib.pyplot as plt

color_x = ["blue","green","yellow","orange","red"]
label_x = ["0 m","10 m","20 m","30 m","40 m"]

for j in range(0,5):

  k=j

  data = np.loadtxt("Intensity_%d.dat"%k)
  
  x = data[:,0]
  y = data[:,1]

  plt.plot(x, y, label = label_x[j],linestyle="-", linewidth=2.0, marker= "", markeredgecolor= color_x[j],markersize=5, color= color_x[j])

plt.xlabel("$t$ [ps]",fontsize=16)
plt.ylabel("$|u|^2$ [W]",fontsize=16)
plt.xlim([-1,2])
plt.ylim([0,2])
plt.legend(numpoints=1,loc="upper right",frameon=False,fontsize=16)
plt.tight_layout()
plt.tick_params(labelsize=16,width=1)
plt.savefig("Plot_Intensity.png")
#plt.show()

