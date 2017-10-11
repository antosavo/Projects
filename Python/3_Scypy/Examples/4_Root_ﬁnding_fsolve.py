import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def f(x):
  return x**3 -2*x**2

#x = scipy.optimize.fsolve(f, 3, xtol = 1e-6)
x = scipy.optimize.fsolve(f, 3) #one root is at x = 2

#print "Root x ~ ", x
print "Root x ~ %.16lf" %x

y = np.linspace(0,3,20)

plt.plot(y,f(y),color = "blue")
plt.plot(y,np.zeros(20),color = "green")

plt.show()

