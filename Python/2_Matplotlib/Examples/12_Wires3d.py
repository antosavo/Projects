import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

plt3d = plt.axes(projection="3d") #To add the third axis to the figure

#u = np.arange(0, np.pi, 0.1)
#v = np.arange(0, 2*np.pi, 0.1)

u = np.linspace(0, np.pi, 30)
v = np.linspace(0, 2 * np.pi, 30)

u, v = np.meshgrid(u, v)

x = np.sin(u)*np.sin(v)
y = np.sin(u)*np.cos(v)
z = np.cos(u)

plt3d.plot_wireframe(x, y, z)
#plt3d.plot_surface(x, y, z, cmap = "hot", rstride = 1, cstride=1, linewidth = 0)

plt3d.set_xlabel("x")
plt3d.set_ylabel("y")
plt3d.set_zlabel("z")

plt3d.set_zlim(-1,1)

plt.savefig("Wires3D.png")
plt.show()
