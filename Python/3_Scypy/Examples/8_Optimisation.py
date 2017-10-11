import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def f(x):
  return np.cos(x) - 3*np.exp(-(x-0.2) ** 2)

# find minima of f(x),
# starting from 1.0 and 2.0 respectively
minimum1 = scipy.optimize.fmin(f, 1.0)
print "Start search at x =1, minimum is", minimum1

minimum2 = scipy.optimize.fmin(f , 2.0)
print "Start search at x =2, minimum is", minimum2

# plot function
x = np.arange(-10, 10, 0.1)
y = f(x)
plt.plot(x, y, label = "$\\cos(x) -3e^{-( x -0.2)^2}$")
plt.xlabel("x")
plt.grid()
plt.axis([ -5 , 5 , -2.2 , 0.5])

# add minimum1 to plot
plt.plot(minimum1, f(minimum1), "vr", label = "minimum 1")

# add start1 to plot
plt.plot(1.0, f(1.0), "or", label = "start 1")

# add minimum2 to plot
plt.plot(minimum2, f(minimum2), "vg", label = "minimum 2")

# add start2 to plot
plt.plot(2.0, f(2.0) , "og", label = "start 2")

plt.legend(numpoints=1, loc = "lower left")
plt.savefig("Optimization.png")
plt.show()

