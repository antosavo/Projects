import numpy as np
import pylab as plt

z = np.arange(0, 1, 0.01)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)

c = x + y

plt.scatter(x, y, c=c)

plt.savefig("Cmap_2.png")
plt.show()
