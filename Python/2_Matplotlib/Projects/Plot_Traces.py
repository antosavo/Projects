import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import LogNorm
#from matplotlib.colors import ListedColormap


data = np.loadtxt("Traces.dat")
#data = np.loadtxt("Test.dat")
x = data[:,0]
y = data[:,1]
z = data[:,2]

#CMAP = LinearSegmentedColormap.from_list('mycmap', [(0, 'blue'),(0.55, 'green'),(0.7, 'yellow'),(1, 'yellow')])
#CMAP = LinearSegmentedColormap.from_list('mycmap', [(0, 'blue'),(0.55, 'green'),(0.7, 'yellow'),(1, 'white')]) #best
#My_Hot = LinearSegmentedColormap.from_list('mycmap', [(0, 'red'),(0.55, 'orange'),(0.7, 'yellow'),(1, 'white')]) 
#plt.pcolormesh(X, Y, Z, cmap=CMAP, vmin=-1, vmax=1)

#plt.pcolormesh(X, Y, Z, cmap='YlGnBu', vmin=-1, vmax=1)
#plt.pcolormesh(X, Y, Z, cmap='jet', vmin=-1, vmax=1)
#plt.pcolormesh(X, Y, Z, cmap='hot', vmin=0, vmax=10)
#colormap_r = ListedColormap(colormap.colors[::-1])


#plt.scatter(x,y,cmap='hot',c=z,marker='.',edgecolor='none',vmin=1, vmax=300)
#plt.scatter(x,y,cmap=CMAP,c=z,marker='.',edgecolor='none',vmin=1, vmax=300,norm = LogNorm())
#plt.scatter(x,y,cmap='hot',c=z,marker='.',edgecolor='none',vmin=1, vmax=300,norm = LogNorm())
#plt.scatter(x,y,cmap=My_Hot,c=z,marker='.',edgecolor='none',vmin=1, vmax=300,norm = LogNorm())
#plt.scatter(x,y,cmap='autumn',c=z,marker='.',edgecolor='none',vmin=1, vmax=300,norm = LogNorm())
#plt.scatter(x,y,cmap='YlOrRd',c=z,marker='.',edgecolor='none',vmin=1, vmax=300,norm = LogNorm())
#plt.scatter(x,y,cmap='hot_r',c=z,marker='.',edgecolor='none',vmin=1, vmax=300,norm = LogNorm())
#plt.scatter(x,y,cmap='YlGnBu',c=z,marker='.',edgecolor='none',vmin=1, vmax=300,norm = LogNorm())
plt.scatter(x,y,cmap='afmhot_r',c=z,marker='.',edgecolor='none',vmin=1, vmax=300,norm = LogNorm(),rasterized=True)


#plt.title('Test')
plt.xlabel('$t$ $[ps]$',fontsize=16)
plt.ylabel('$z$ $[m]$',fontsize=16)
plt.xlim([40,55])
plt.xticks([42,44,46,48,50,52,54],['2','4','6','8','10','12','14'])
plt.ylim([0,1500])
plt.yticks([0,250,500,750,1000,1250,1500])
#cbar.ax.set_yticklabels(['0','1','2','>3'])
#cbar.set_label('# of contacts', rotation=270)
cbar=plt.colorbar()
cbar.set_label('$|u|^2$ $[W]$',fontsize=16)

#plt.yscale('log')
#plt.tick_params(labelsize=16,width=1)



plt.savefig('Traces.png')
#plt.show()