import numpy as np

x = np.array([0,0.5,1.0,1.5])

print "x = ", x

y = np.arange(0,10,1)

print "y = ", y

u = np.linspace(0, 2*np.pi, 4)

print "u = ", u

z = np.zeros(4)

print "z = ", z

z[0] = 3.5
z[2] = 4

print "z = ", z

print "z[0] = ", z[0]

print "z[0:3] = ", z[0:3]

print "z^2 = ", z**2

print "z + 10 = ", z + 10

print "sin(z) = ", np.sin(z)