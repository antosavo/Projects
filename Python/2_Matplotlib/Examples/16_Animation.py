import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

x = np.linspace(0, 2 * np.pi, 120)

def f(x):
    return np.sin(x)

def updatefig(i):
    global x
    if i==0:
	im = plt.plot(x,f(x + i*(np.pi/15.)),color="blue", linestyle ="--")
    else:
	im = plt.plot(x,f(x + i*(np.pi/15.)),color="red")
    return im

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)

plt.xlabel("x")
plt.xlim([0,2*np.pi])
plt.ylabel("y")
plt.ylim([-1,1])

plt.show()

ani.save("Animation.mp4")
