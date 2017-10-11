import numpy as np
#import pylab as plt
import matplotlib.pyplot as plt

x = np.arange(-3.14,3.14,0.01)
y = np.sin(x)

plt.plot(x, y, label="sin(x)")
plt.legend()
plt.savefig("Plot.png")
plt.show()