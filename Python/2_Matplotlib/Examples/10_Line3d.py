import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

plt3d = plt.axes(projection="3d") #To add the third axis to the figure

z = np.arange(0, 1, 0.01)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)

plt3d.plot(x, y, z, color = "blue")

plt3d.set_xlabel("x")
plt3d.set_ylabel("y")
plt3d.set_zlabel("z")

plt.savefig("Line3D.png")
plt.show()
