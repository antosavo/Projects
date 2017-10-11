import mahotas as mh
from mahotas.features import surf
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

image = mh.imread('cat.jpg', as_grey=True)

print 'Image matrix:\n', image
print 'Image shape:',image.shape
print 'Image vector:', image.reshape(image.shape[0]*image.shape[1])
print 'Scaled Image vector:', scale(image.reshape(image.shape[0]*image.shape[1])) #centers to the mean and scales to unit variance.

plt.gray()
plt.imshow(image)
plt.show()

#Speeded-Up Robust Features (SURF) is a method of extracting interesting points of an image
#and creating descriptions that are invariant of the image's scale, orientation, and illumination.

print 'The first SURF descriptor:\n', surf.surf(image)[0]
print 'Extracted %s SURF descriptors' % len(surf.surf(image))
