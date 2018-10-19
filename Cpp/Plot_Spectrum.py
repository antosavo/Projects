import numpy as np
import matplotlib.pyplot as plt

k=4

data = np.loadtxt("Spectrum_%d.dat"%k)
  
x = data[:,0]
y = data[:,1]
z = data[:,2]

#Plot

#plt.clf() # Clear the figure
plt.title("Spectrum",fontsize=16)
plt.xlabel("$\\omega [1/ps]$",fontsize=16)
plt.ylabel("$|u_r|^2+|u_r|^2$",fontsize=16)
plt.xlim([-200,200])
#plt.xticks([0,90,180,270,360],["$0$","$\\frac{1}{2}\\pi$","$\\pi$","$\\frac{3}{2}\\pi$","$2$$\\pi$"])
plt.ylim([0.00001,10000])
plt.yscale("log")
#plt.yticks([-0.05,0.00,0.05,0.10,0.15,0.20,0.25],["-0.05","0.00","0.05","0.10","0.15","0.20","0.25"])
plt.tick_params(labelsize=16,width=1)

plt.plot(x, y**2 + z**2, label = "spectrum",linestyle="-", linewidth=2.0, marker= "", color= "red")
plt.legend(numpoints=1,loc="upper right",frameon=False,fontsize=16)
plt.tight_layout()

plt.savefig("Plot_Spectrum.png")
#plt.show()

