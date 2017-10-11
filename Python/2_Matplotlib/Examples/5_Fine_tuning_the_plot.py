#import pylab as plt
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3.14,3.14,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize = (6,5))
plt.plot(x, y1, label = "sin(x)", linestyle="--", linewidth=2.0, color = "red")
plt.plot(x, y2, label = "cos(x)", linestyle=" ", marker = "o", color = "green", markeredgecolor='none')
plt.legend(loc="upper left",frameon=False)
#plt.grid()
plt.xlabel("x")
plt.xlim([-3.2,3.2])
plt.ylabel("y")
plt.ylim([-1,1.2])
plt.xticks([-3.14,0,3.14],["$-\\frac{1}{2}\\pi$","$0$","$\\frac{1}{2}\\pi$"])
plt.title("This is the title of the graph ")
plt.savefig("FTPlot.png")
plt.show()
