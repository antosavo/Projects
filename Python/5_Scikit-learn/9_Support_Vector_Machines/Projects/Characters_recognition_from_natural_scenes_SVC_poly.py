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

for j in range(1,11):
  for k in range(1,31):
    if j<=9 and k<=9:
      image_filename = 'Characters_from_natural_scenes/Sample00%d/img00%d-0000%d.png'%(j,j,k)
    if j<=9 and k>9:
      image_filename = 'Characters_from_natural_scenes/Sample00%d/img00%d-000%d.png'%(j,j,k)
    if j>9 and k<=9:
      image_filename = 'Characters_from_natural_scenes/Sample0%d/img0%d-0000%d.png'%(j,j,k)
    if j>9 and k>9:
      image_filename = 'Characters_from_natural_scenes/Sample0%d/img0%d-000%d.png'%(j,j,k)
    image = misc.imread(image_filename, flatten=True)#reading the image
    #making a 90 x 60 image
    h = 91.0/image.shape[0]
    l = 61.0/image.shape[1]
    image = ndimage.zoom(image,(h,l))
    image = scale(image[0:90,0:60].reshape(90*60))
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
classifier = svm.SVC(kernel='poly', degree=2, C=2) #degree = 3, C=0.1
classifier.fit(X_train_reduced, y_train)
print 'Accuracy = #Correct/#Instances:', classifier.score(X_test_reduced, y_test)

print '\nTraining the classifier on the unreduced data...'
classifier = svm.SVC(kernel='poly', degree=2, C=2)
classifier.fit(X_train, y_train)
print 'Accuracy = #Correct/#Instances:', classifier.score(X_test, y_test)


'''
print '\nFinding best parameters for the unreduced data...'

model = svm.SVC(kernel='poly')
parameters = {'degree': (1, 2, 3, 4), 'C': ( 1, 2, 5, 10)} #degree = 2, C=2

grid_search = GridSearchCV(model, parameters, n_jobs=4, scoring='accuracy')
grid_search.fit(X, y)

print 'Best score:', grid_search.best_score_
print 'Best params:', grid_search.best_params_
'''







