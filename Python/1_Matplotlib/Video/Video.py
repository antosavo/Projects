import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

def updatefig(k):
    data = np.loadtxt("Intensity_%d.dat"%k)
    x = data[:,0]
    y = data[:,1]
    if k==0:
	im = plt.plot(x, y, color="blue", linestyle ="-")
    else:
	im = plt.plot(x, y, color="red")
    return im

ani = animation.FuncAnimation(fig, updatefig, interval=100,frames=5, blit=True)

plt.xlabel("x")
plt.xlim([-10,30])
plt.ylabel("y")
plt.ylim([0,10])

plt.show()

ani.save("Animation.mp4")
