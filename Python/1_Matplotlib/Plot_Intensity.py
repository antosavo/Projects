import numpy as np
import matplotlib.pyplot as plt

color_x = ["blue","green","yellow","orange","red"]
label_x = ["z1","z2","z3","z4","z5"]

for j in range(0,5):

  k=j*250

  data = np.loadtxt("Intensity_12_%d.dat"%k)
  
  x = data[:,0]
  y = data[:,1]

#Plot

  #plt.clf() # Clear the figure
  plt.title("Intensity",fontsize=16)
  plt.xlabel("$t$",fontsize=16)
  plt.ylabel("$|u|^2$",fontsize=16)
  plt.xlim([-5,35])
  #plt.xticks([0,90,180,270,360],["$0$","$\\frac{1}{2}\\pi$","$\\pi$","$\\frac{3}{2}\\pi$","$2$$\\pi$"])
  plt.ylim([0.00001,11])
  plt.yscale("log")
  #plt.yticks([-0.05,0.00,0.05,0.10,0.15,0.20,0.25],["-0.05","0.00","0.05","0.10","0.15","0.20","0.25"])
  plt.tick_params(labelsize=16,width=1)

  plt.plot(x, y, label = label_x[j],linestyle="-", linewidth=2.0, marker= "", markeredgecolor= color_x[j],markersize=5, color= color_x[j])
  plt.legend(numpoints=1,loc="upper right",frameon=False,fontsize=16)
  plt.tight_layout()

plt.savefig("Intensity.png")
#plt.show()

