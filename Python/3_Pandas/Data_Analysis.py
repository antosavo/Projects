import numpy as np
import pandas as pd
import pylab as plt

phi = np.zeros(31)
DE = np.zeros(31)

for i in range(0,31):
  k=i*12
  df = pd.read_table('phi_%d/Energy_Transfer.dat'%k, sep='\t', header=None)
  phi[i] = i*12.0 #[col][row]
  DE[i] = df[2][4] #[col][row]

beta2 = -2.6*(10**-4)
beta3 = 3.5*(10**-5)
gamma = 0.01
alfa = 0.5

P1 = 20.0
P2 = 10.0

O1= -np.sqrt(-alfa*gamma*P1/beta2)
T1= np.sqrt((-beta2-beta3*O1)/(gamma*P1))

O2= -np.sqrt(-alfa*gamma*P2/beta2)
T2= np.sqrt((-beta2-beta3*O2)/(gamma*P2))

Gain = (DE - (2*T1*P1 - 2*T2*P2) )/(2*T2*P2) 

data = pd.read_table('Gain_Radiation_NLSE.dat', sep='\t', header=None) #data frame

plt.plot(phi, Gain, label ="Theory", color = "red" )
plt.plot(data[0], data[1], label ="gNLSE", color = "blue" )
plt.xlim([0,360])
plt.xticks([0,90,180,270,360],['$0$','$\\frac{1}{2}\\pi$','$\\pi$','$\\frac{3}{2}\\pi$','$2$$\\pi$'])
plt.xlabel("$\\phi$",fontsize=14)
plt.ylim([-1,1])
plt.ylabel('$\\Delta$$E_1$/$E_2$',fontsize=14)
plt.legend()
plt.savefig("Energy_transfer.png")
plt.show()