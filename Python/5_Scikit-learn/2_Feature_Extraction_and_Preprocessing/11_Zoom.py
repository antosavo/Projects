import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage


image = misc.imread('O.png', flatten=True)#.reshape(900*1200)

print "shape:", image.shape

image = ndimage.zoom(image, (2,0.5))

print "zoomed shape:", image.shape

plt.gray()
plt.imshow(image)
plt.show()