import numpy as np
#import pylab as plt
import matplotlib.pyplot as plt
#subplot( numRows, numCols, plotNum)

t = np.arange( 0, 2*np.pi, 0.01)

plt.subplot( 2, 1, 1)
plt.plot(t, np.sin(t))
plt.xlabel("t")
plt.ylabel("sin(t)")

plt.subplot( 2, 1, 2)
plt.plot(t, np.cos(t))
plt.xlabel("t")
plt.ylabel("cos(t)")

plt.show()

