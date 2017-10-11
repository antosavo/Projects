import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage
from sklearn.preprocessing import scale
from sklearn.manifold import Isomap
import time

print '\nLoading the images...'

X = []
y = []


for j in range(1,11):#63
  for k in range(1,56):#56
    if j<=9 and k<=9:
      image_filename = 'Hand-drawn_characters/Sample00%d/img00%d-00%d.png'%(j,j,k)
    if j<=9 and k>9:
      image_filename = 'Hand-drawn_characters/Sample00%d/img00%d-0%d.png'%(j,j,k)
    if j>9 and k<=9:
      image_filename = 'Hand-drawn_characters/Sample0%d/img0%d-00%d.png'%(j,j,k)
    if j>9 and k>9:
      image_filename = 'Hand-drawn_characters/Sample0%d/img0%d-0%d.png'%(j,j,k)
    image = misc.imread(image_filename, flatten=True)#reading the image
    image = misc.imresize(image,0.20)#resizing 0.20 => from 900*1200 to 180*240
    #finding the object
    image2 = image - image.max()
    objs = ndimage.find_objects(image2)
    image = image[int(objs[0][0].start):int(objs[0][0].stop),int(objs[0][1].start):int(objs[0][1].stop)]
    #zooming to 90x60
    h = 91.0/image.shape[0]
    l = 61.0/image.shape[1]
    image = ndimage.zoom(image,(h,l))
    image = scale(image[0:90,0:60].reshape(90*60))
    #image = image[0:90,0:60].reshape(90*60)
    #creating the features
    X.append(image)
    y.append(j)

X = np.array(X)

print '\nReducing the dimensions ...'
start = time.time()

imap = Isomap(n_components=2, n_neighbors=5)
X_reduced = imap.fit_transform(X)

end = time.time()
print 'Time:', end - start

print 'Shape X:', X.shape
print 'Shape X_reduced:', X_reduced.shape

plt.scatter(X_reduced[:,0], X_reduced[:,1], cmap = "jet", c = y, marker = "o", edgecolor = "none", s = 40*np.ones(550), vmin = 0, vmax = 9)
cbar = plt.colorbar()
cbar.set_label("N")
cbar.set_ticks([0,1,2,3,4,5,6,7,8,9])
plt.savefig('Isomap_H.png')
plt.show()