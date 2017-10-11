import numpy as np
import scipy.integrate
#import pylab as plt
import matplotlib.pyplot as plt

def f(y,t): 
  """ this is the rhs of the ODE to integrate , i.e. dy/dt = f(y,t) """
  return -2*y*t

y0 = 1 #initial value
a = 0  # integration limits for t
b = 2

t = np.linspace(a, b, 100)
y = scipy.integrate.odeint(f, y0, t)

plt.plot(t, y)
plt.xlabel("t")
plt.ylabel("y(t)")
plt.show()
