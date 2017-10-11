import numpy as np
from scipy.ndimage.interpolation import shift

xs = np.array([ 0,1,2,3,4,5,6,7,8,9])

print "original:", xs

print "shifted:", shift(xs,3)

print "rolled:", np.roll(xs, 2) #np.roll(a, shift, axis=None)