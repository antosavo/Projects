import math 
import numpy as np
#import pylab as plt
import matplotlib.pyplot as plt

x = np.arange(-math.pi, math.pi, 0.01)
y = np.arange(-math.pi, math.pi, 0.01) 

X, Y = np.meshgrid(x,y)
Z = np.sin(X)
  
plt.scatter(X, Y, cmap = "jet", c = Z, marker = ".", edgecolor = "none", vmin = -1, vmax = 1)
#cmap = "afmhot_r","afmhot","cool", ...
cbar = plt.colorbar()
cbar.set_label("Z")
cbar.set_ticks([-1.0,-0.5,0.0,0.5,1.0])

plt.xlabel("X")
plt.xlim([-math.pi, math.pi])
plt.ylabel("Y")
plt.ylim([-math.pi, math.pi])
plt.savefig("Cmap_1.png")
plt.show()