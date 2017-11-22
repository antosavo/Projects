import pandas as pd
import pylab as plt

frame= pd.read_csv('a_b.dat', sep='\t')
print "\nDF:\n\n", frame

z = frame['z']
a_CM = frame['a_CM']
a_NLSE = frame['a_NLSE']
b_CM = frame['b_CM']
b_NLSE = frame['b_NLSE']

plt.title('a Weibull fit')
plt.plot(z, a_CM, 'sr', label = 'a CM')
plt.plot(z, a_NLSE, 'sb', label = 'a NLSE')
plt.xlabel('z [m]')
plt.ylabel('a')
plt.legend(numpoints=1)
plt.savefig('a.png')

plt.clf()
plt.title('b Weibull fit')
plt.plot(z, b_CM, 'sr', label = 'b CM')
plt.plot(z, b_NLSE, 'sb', label = 'b NLSE')
plt.xlabel('z [m]')
plt.ylabel('b')
plt.legend(numpoints=1)
plt.savefig('b.png')

frame.to_csv("frame.dat", sep='\t')