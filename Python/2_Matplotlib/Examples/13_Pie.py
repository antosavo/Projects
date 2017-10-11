import numpy as np
import matplotlib.pyplot as plt

fracs = [30, 15, 45, 10]
colors = ['b', 'g', 'r', 'w']

plt.pie(fracs, colors = colors, labels=['A', 'B', 'C', 'D'])

plt.savefig("Pie.png")
plt.show()