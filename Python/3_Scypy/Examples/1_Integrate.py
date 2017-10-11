import numpy as np
import scipy.integrate

def f(x):
  return np.cos(x)

Integral_f, Error = scipy.integrate.quad(f, 0, 0.5*np.pi) #Integration of a function

print "Integral_f = ", Integral_f
print "Error = ", Error

x = np.linspace(0,0.5*np.pi,200)
y = f(x)

Integral_n = scipy.integrate.simps(y, x) #Numerical integration

print "Integral_n = ", Integral_n

Integral_x = scipy.integrate.cumtrapz(y, x) #I(x) with x between 0 and x_max

print "Integral_x = ", Integral_x