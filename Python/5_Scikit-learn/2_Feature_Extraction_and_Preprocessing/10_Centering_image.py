import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage


image = misc.imread('O.png', flatten=True)#.reshape(900*1200)

image = misc.imresize(image,0.20)

image = image - image.max()


print "shape=", image.shape #(180, 240)


objs = ndimage.find_objects(image)


x_cm = 0.5*(objs[0][0].stop + objs[0][0].start)

y_cm = 0.5*(objs[0][1].stop + objs[0][1].start)


image = np.roll(image, int(0.5*image.shape[0] - x_cm), axis=0)

image = np.roll(image, int(0.5*image.shape[1] - y_cm), axis=1)

#image = image[(x_cm-80):(x_cm+80),(y_cm-70):(y_cm+70)]

#print image

plt.gray()
plt.imshow(image)
plt.show()
