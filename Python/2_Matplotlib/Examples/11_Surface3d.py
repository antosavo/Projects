import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

plt3d = plt.axes(projection="3d") #To add the third axis to the figure

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(R)

surf = plt3d.plot_surface(X, Y, Z, cmap = "hot", rstride = 1, cstride=1, linewidth = 0)

plt3d.set_xlabel("x")
plt3d.set_ylabel("y")
plt3d.set_zlabel("z")
#plt3d.view_init(elev=0, azim=180)

plt3d.set_zlim(-1,1)

cbar = plt.colorbar(surf)
cbar.set_label("Z")
cbar.set_ticks([-1.00,-0.75,-0.50,-0.25,0.00,0.25,0.50,0.75,1.00])

plt.savefig("Surface3D.png")
plt.show()
