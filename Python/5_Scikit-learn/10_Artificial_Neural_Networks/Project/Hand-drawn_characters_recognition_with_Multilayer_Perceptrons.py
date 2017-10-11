import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

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
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=3)


n_components = 20 #variance ratio >=0.01
print '\nReducing the dimensions ...'
pca = PCA(n_components=n_components)
X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)
print 'Variance ratio:', pca.explained_variance_ratio_
print 'Shape X_train:', X_train.shape
print 'Shape X_train_reduced:', X_train_reduced.shape
print 'Shape X_test:', X_test.shape
print 'Shape X_test_reduced:', X_test_reduced.shape


clf = MLPClassifier(hidden_layer_sizes = (100), solver='lbfgs')# 100 95%
clf.fit(X_train, y_train)

print 'Accuracy:', clf.score(X_test, y_test)

y_pred = clf.predict(X_test)

table = pd.crosstab(np.array(y_test), y_pred, rownames=['Actual'], colnames=['Predictions'])
print table
