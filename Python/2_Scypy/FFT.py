import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack 

k = 1000

tm = 160.0  
m = 15
nt = 2**m
dt= tm/(nt-1)

data = np.loadtxt("Amplitude_%d.dat"%k)
  
t = data[:,0]
Ar = data[:,3]
Ai = data[:,4]

A = Ar + 1j*Ai

S = scipy.fft(A)

freqs = -1*scipy.fftpack.fftfreq(nt,dt)

S_r = S.real
S_i = S.imag

#Plot
plt.title("Spectrum")
plt.xlabel("$\\omega [1/ps]$")
plt.ylabel("$|u_r|^2+|u_r|^2$")
plt.xlim([-100,100])
plt.plot(2*np.pi*freqs, S_r**2 + S_i**2, label = "FFT",linestyle="-", linewidth=2.0, marker= "", color= "red")
plt.legend(numpoints=1,loc="upper left",frameon=False,fontsize=16)
plt.tight_layout()

plt.savefig("FFT.png")
plt.show()