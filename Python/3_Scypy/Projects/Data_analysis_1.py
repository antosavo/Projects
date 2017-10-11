import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chisquare

Dist = 1500
Name = 'NLSE'

#data = np.loadtxt("PDF_500_NLSE_log.dat")
data = pd.read_csv("PDF_%d_%s_log.dat"%(Dist,Name), sep ='\t', header=None)
x = data[0]
y = data[1]

data2 = pd.read_csv("PDF_%d_%s.dat"%(Dist,Name), sep ='\t', header=None)
x2 = data2[0]
y2 = np.log(data2[1]+0.0000001)

#Fits

def f(x, a, b, c):#function to fit
  return c-(x/a)**b

#init_vals = [10, 1, -10]
#params, covar = curve_fit(f, x, y,p0=init_vals)

params, pcov = curve_fit(f, x, y)

print '\n', 'a=', params[0], 'b=', params[1],  'c=', params[2]

#Plots

plt.clf() # Clear the figure
plt.title('Plot Fit',fontsize=20)
plt.xlabel('$|u|^2$',fontsize=20)
plt.ylabel('log(PDF)',fontsize=20)
plt.plot(x, y, label = 'Data',linestyle='', marker='o', color='g')
plt.plot(x, f(x, *params),label = 'Fit',linestyle='--', color='b')
plt.legend()
plt.savefig('Fit_py_%s.png'%Name)

#

#chisquare
chi_2 = chisquare(y2, f(x2, *params))[0][1]/(x2.count()-3)

print "chisquare=", chi_2
print "nu=", x2.count()-3

#
fitted_p = {
	'params': [ params[0], params[1], params[2]],
	'sdv': [np.sqrt(pcov[0][0]),np.sqrt(pcov[1][1]),np.sqrt(pcov[2][2])],
	'chi_2': [chi_2,chi_2,chi_2]
}

fp = pd.DataFrame(fitted_p, index=['a','b','c'])
fp.to_csv("Fitting_parameters_%s_chi_2.dat"%(Name),sep='\t')

  
