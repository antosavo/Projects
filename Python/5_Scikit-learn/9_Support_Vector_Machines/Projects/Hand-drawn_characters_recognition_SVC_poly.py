import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage
from sklearn.preprocessing import scale
from sklearn.cross_validation import train_test_split
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn.grid_search import GridSearchCV

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
    #image = scale(image[0:90,0:60].reshape(90*60))
    image = image[0:90,0:60].reshape(90*60)
    #creating the features
    X.append(image)
    y.append(j)

X = np.array(X)
X_train, X_test, y_train, y_test = train_test_split(X, y)



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

print '\nTraining the classifier on the reduced data..'
classifier = svm.SVC(kernel='poly', degree=2, C=0.05) #degree = 3, C=0.1
classifier.fit(X_train_reduced, y_train)
print 'Accuracy = #Correct/#Instances:', classifier.score(X_test_reduced, y_test)

print '\nTraining the classifier on the unreduced data...'
classifier = svm.SVC(kernel='poly', degree=2, C=0.05)
classifier.fit(X_train, y_train)
print 'Accuracy = #Correct/#Instances:', classifier.score(X_test, y_test)

'''
print '\nFinding best parameters for the unreduced data...'

model = svm.SVC(kernel='poly')
parameters = {'degree': (1, 2, 3, 4), 'C': (0.05, 0.1, 0.15)} #degree = 2, C=0.05

grid_search = GridSearchCV(model, parameters, n_jobs=4, scoring='accuracy')
grid_search.fit(X, y)

print 'Best score:', grid_search.best_score_
print 'Best params:', grid_search.best_params_
'''


