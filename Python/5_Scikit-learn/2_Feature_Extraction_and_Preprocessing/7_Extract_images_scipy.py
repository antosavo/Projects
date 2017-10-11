from scipy import misc
from scipy import ndimage
from sklearn.cluster import spectral_clustering
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
import numpy as np

image = misc.imread('cat.jpg', flatten=True)#flatten=True => gray-scale

print 'Image matrix:\n', image
print 'Image shape:',image.shape
print 'Image vector:', image.reshape(image.shape[0]*image.shape[1])
print 'Scaled Image vector:', scale(image.reshape(image.shape[0]*image.shape[1])) #centers to the mean and scales to unit variance.

plt.gray()
plt.imshow(image) # cmap=plt.cm.gray)
plt.show()

#Slicing
misc.imsave('image_sliced.png', image[150:300,200:400]) 

#Resizing
resized_image = misc.imresize(image,0.20)

print 'Resized image shape:', resized_image.shape

misc.imsave('image_resized.png', resized_image)

#Center of mass

print 'Center of Mass:', ndimage.measurements.center_of_mass(image)

#Cropping
lx, ly = image.shape

misc.imsave('image_cropped.png', image[lx / 4: - lx / 4, ly / 4: - ly / 4])

#Filtering
filtered_image = ndimage.uniform_filter(image, size=11)

print 'Filtered image shape:', filtered_image.shape

misc.imsave('image_filtered.png', filtered_image)

#Edge detection
sx = ndimage.sobel(image, axis=0, mode='constant')
sy = ndimage.sobel(image, axis=1, mode='constant')
image_edges = np.hypot(sx, sy)

misc.imsave('image_edges.png', image_edges)






