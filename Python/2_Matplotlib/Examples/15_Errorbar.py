import math
import numpy as np
import matplotlib.pyplot as plt

#x = np.arange(-3.14,3.14,0.2)
x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x)
#dy = 0.1
#dy = 0.1*np.ones(20)
dy = np.random.uniform(0,0.1,20)

plt.errorbar(x,y,dy, linestyle="", marker = ".")

plt.xlim([-0.1,2*np.pi+0.1])

plt.savefig("Errorbar.png")
plt.show()