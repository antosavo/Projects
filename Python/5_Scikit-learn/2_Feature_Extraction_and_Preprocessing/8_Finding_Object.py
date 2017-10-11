import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage


image = misc.imread('O.png', flatten=True)#.reshape(900*1200)

image = misc.imresize(image,0.20)

image = image - image.max()

objs = ndimage.find_objects(image)

# Get the height and width
height = int(objs[0][0].stop - objs[0][0].start)
width = int(objs[0][1].stop - objs[0][1].start)

image = image[objs[0][0].start:objs[0][0].stop,objs[0][1].start:objs[0][1].stop]

#print image

plt.gray()
plt.imshow(image)
plt.show()
