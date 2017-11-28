import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Epsilon.dat")
x = data[:,0]
y = data[:,1]
Dy = data[:,2]

#Plot
#plt.clf() # Clear the figure
plt.title('Epsilon',fontsize=20)
plt.xlabel('$\\beta_{3rel}$/$\\beta_{3}$',fontsize=16)
plt.ylabel('$\\epsilon_{rel}$/$\\epsilon$',fontsize=16)
plt.xlim([0,1.5])
plt.ylim([0.0,0.002])
#plt.yscale('log')
plt.tick_params(labelsize=16,width=1)

#plt.scatter(x, y,label = 'Data',marker='o', color='b',s=50)
plt.errorbar(x, y,yerr=Dy,label = 'Data',fmt='-o',color='blue') #fmt='o' for data, fmt='-o' for data + line
#plt.plot(x, y, label = 'Data',linestyle='', marker='o',markersize=5, color='b')

plt.legend(numpoints=1,loc="upper left",frameon=False)
plt.tight_layout()

plt.savefig('Epsilon.png')
plt.show()

