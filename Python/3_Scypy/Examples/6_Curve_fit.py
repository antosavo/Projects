import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize 
#from scipy.optimize import curve_fit

#data = np.loadtxt("Data.dat")
#x = data[:,0]
#y = data[:,1]

x = np.linspace(0,4,50)

def f(x, a, b, c):
  return a*np.exp(-b*x)+c

y = f(x, 2.5, 1.3, 0.5)

yi = y + 0.2*np.random.normal(size=len(x)) #mu=0, sigma=1

params, cov = scipy.optimize.curve_fit(f, x, yi)
#a, b, c= params

#init_vals = [1.5, 1, 0.5]
#params, cov = scipy.optimize.curve_fit(f, x, yi,p0=init_vals) #by default the initial values are 1,1,1
#a, b, c= params

print "Fitted params:", params
print "Variance:", np.diagonal(cov)

np.savetxt("Fitting_parameters.dat",params, newline = "\t") # It can print just numpy array
#np.savetxt("Fitting_parameters.dat",params,fmt="%lf") # format longfloat

plt.plot(x, yi, linestyle= "", marker = "o", label = "data $y_i$")
plt.plot(x, f(x,*params), linestyle= "-", label = "fit $f(x_i)$") #f(x,*params)=f(x,a,b,c)
#plt.plot(x, f(x,a,b,c), linestyle= "-", label = "fit $f(x_i)$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("Fit.png")
plt.show()