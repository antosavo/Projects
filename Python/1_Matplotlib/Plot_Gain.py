import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

color_x = ['red','orange','green','blue']
label_x = ['0.00','0.02','0.04','0.06']

plt.title('Gain',fontsize=20)
plt.xlabel('$\\phi$',fontsize=16)
plt.ylabel('$\\Delta$$E_1$/$E_2$',fontsize=16)
plt.xlim([0,360])
plt.xticks([0,90,180,270,360],['$0$','$\\frac{1}{2}\\pi$','$\\pi$','$\\frac{3}{2}\\pi$','$2$$\\pi$'])
plt.ylim([-0.15,0.20])
plt.tick_params(labelsize=20,width=1)

def f(x, a, b, c):#function to fit
    return a + b*np.sin((x-c)*np.pi/180)

for j in range(0,4):
    k=j*2
    df = pd.read_csv('P-100-10_Dz_0_%d/Gain_Radiation_E.dat'%k,sep='\t',header=None)
    x = df.iloc[:,0]
    y = df.iloc[:,1]
    
    params, pcov = curve_fit(f, x, y)
    
    plt.scatter(x, y, marker= 'o', s=20, c= color_x[j], label=None)
    plt.plot(x, f(x, *params), linestyle='--', c= color_x[j],  label = '$\\delta$ = '+label_x[j] +' m')
    
plt.legend(numpoints=1,loc="upper right",frameon=False,fontsize=14)
plt.savefig('Gain.png')
plt.show()
