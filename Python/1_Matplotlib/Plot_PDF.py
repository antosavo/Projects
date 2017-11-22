import numpy as np
import math
import matplotlib.pyplot as plt


#x_1= np.arange(0.0010, 0.0020, 0.00001) 
#x_1 = np.zeros(31) # y data array

marker_x = ['o','*','v','s','^']
color_x = ['blue','green','cyan','orange','red']
label_x = ['100','200','500','1000','1500']

for j in range(0,5):

  print 'j=',j,'\n'

  
  file_name ='PDF_'+label_x[j]+'.dat'
  #data = np.loadtxt("PDF_100.dat"%k[j])
  data = np.loadtxt(file_name)

  x = data[:,0]
  y = data[:,1]

  #plt.clf() # Clear the figure
  plt.title('PDF',fontsize=20)
  plt.xlabel('$|u|^2$',fontsize=20)
  plt.ylabel('$PDF$',fontsize=20)
  plt.xlim([0,1000])
  #plt.xticks([0,90,180,270,360],['$0$','$\\frac{1}{2}\\pi$','$\\pi$','$\\frac{3}{2}\\pi$','$2$$\\pi$'])
  plt.ylim([0.0000001,1])
  #plt.yticks([-0.05,0.00,0.05,0.10,0.15,0.20,0.25],['-0.05','0.00','0.05','0.10','0.15','0.20','0.25'])
  plt.yscale('log')
  plt.tick_params(labelsize=16,width=1)

  #plt.scatter(x, y,label = 'Data',marker='o', color='b',s=50)
  #plt.errorbar(x, y,yerr=Dy,label = 'Data',fmt='-o',color='b') #fmt='o' for data, fmt='-o' for data + line
  #plt.plot(x, y, label = '$\\delta_1$-$\\delta_2$',linestyle='', marker='o', color='blue')
  plt.plot(x, y, label = label_x[j],linestyle='', marker= marker_x[j], markeredgecolor= color_x[j],markersize=5, color= color_x[j])
  #plt.plot(x, f(x, *params),label = 'Fit',linestyle='--', color='blue')
  #plt.plot(x, f(x, *params),linestyle='--', color= color_x[j])
  #plt.legend()
  #plt.legend(scatterpoints=1,loc="upper left",frameon=False)
  plt.legend(numpoints=1,loc="upper right",frameon=False,fontsize=16)
  plt.tight_layout()

plt.savefig('PDF.png')
plt.show()

