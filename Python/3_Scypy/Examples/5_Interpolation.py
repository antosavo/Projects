import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

x = np.linspace(0,5,10)
y = -x**2
y += np.random.uniform(-1.5, 1.5, len(x))

xfine = np.linspace (0, 5, 100)
y0 = scipy.interpolate.interp1d (x, y, kind = "nearest")
y1 = scipy.interpolate.interp1d (x, y, kind = "linear")
y2 = scipy.interpolate.interp1d (x, y, kind = "quadratic")

plt.plot(x, y, marker = "o", linestyle = "", color = "blue", label = "data point")
plt.plot(xfine, y0(xfine), linestyle = "-", color = "green", label = "nearest")
plt.plot(xfine, y1(xfine), linestyle = "-", color = "red", label = "linear")
plt.plot(xfine, y2(xfine), linestyle = "-", color = "cyan", label = "quadratic")
plt.title("Interpolation")
plt.xlim([-1,6])
plt.xlabel("x")
plt.legend()
plt.savefig("Interpolation.png")
plt.show()
