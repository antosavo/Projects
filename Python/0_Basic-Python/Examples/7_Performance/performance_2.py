import time
import numpy as np

v = np.zeros(10)
w = np.ones(10)
I = np.eye(10) # Matrix I
i=0
j=0

start = time.time()

while (i < 10):
    while (j < 10):
        w[i] += I[i][j]*v[j]
        j += 1  
    i += 1 

end = time.time()

t = end - start
print "np :", t
