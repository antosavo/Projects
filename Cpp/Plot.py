import numpy as np
import pylab as plt

data = np.loadtxt("Autocorr.dat")
x = data[:,0]
y = data[:,1]

xm=1
#plt.clf() # Clear the figure
plt.title('Autocorrelation',fontsize=20)
plt.xlabel('$t$',fontsize=20)
plt.ylabel('$Ac(t)/Ac(0)$',fontsize=20)
plt.xlim([0,xm])
plt.ylim([-0.5,1.1])
#plt.set_yscale('log')
plt.tick_params(labelsize=16,width=1)

plt.scatter(x, y,label = 'Data',marker='o', color='red',s=30)
plt.legend(scatterpoints=1,loc="upper left",frameon=False)
#plt.legend(numpoints=1,loc="upper left",frameon=False)
plt.savefig('Autocorr_%d.png'%xm)

