import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


x = np.array ([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array ([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])


def f(x, a_0, a_1, a_2, a_3):#function to fit
  return a_0 + a_1*x + a_2*x**2 +a_3*x**3

a, cov_a = curve_fit(f, x, y)

print "a = ", a


sigma_a_2 = np.diagonal(cov_a)

print "(sigma_a)^2 = ", sigma_a_2


xs = np.arange(0,5,0.1)

plt.plot( x, y,linestyle='',marker = "o",label = "data")
plt.plot( xs, f(xs,*a),label = "fitted curve")
plt.ylabel("y")
plt.xlabel("x")
plt.legend()
plt.savefig("polyfit.png")
plt.show()

