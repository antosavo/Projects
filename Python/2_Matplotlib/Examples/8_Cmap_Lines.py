import numpy as np
import matplotlib.pyplot as plt

colors = plt.cm.jet(np.linspace(0,1,10))

print 'colors:', colors

x = np.linspace(0,1,50)

for i in range(0,10):
  y = np.ones(len(x))*i
  plt.plot(x, y, c = colors[i], label = i )

plt.legend(loc="upper left")
plt.ylim(-1,10)
plt.savefig("Cmap_Lines.png")
plt.show()
