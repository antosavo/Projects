import numpy as np
from scipy import misc
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import scale
import pyprind

pbar = pyprind.ProgBar(400)

print '\nLoading the images...'
X = []
y = []

for j in range(1,41):
  for k in range(1,11):
    image_filename = 'faces/s%d/%d.pgm'%(j,k)
    X.append(scale(misc.imread(image_filename, flatten=True).reshape(10304)))
    #every image is im.shape => (1, 112, 92) = 10304
    #scale: centers to the mean and scales to unit variance.
    y.append('s%d'%j)
    pbar.update()

X = np.array(X)
X_train, X_test, y_train, y_test = train_test_split(X, y)

n_components = 16 #variance_ratio <=0.01
print '\nReducing the dimensions...'
pca = PCA(n_components=n_components)
X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)
print 'Variance ratio:', pca.explained_variance_ratio_
print 'Shape X_train:', X_train.shape
print 'Shape X_train_reduced:', X_train_reduced.shape
print 'Shape X_test:', X_test.shape
print 'Shape X_test_reduced:', X_test_reduced.shape

print '\nTraining the classifier on the reduced data...'
classifier = LogisticRegression()
classifier.fit(X_train_reduced, y_train)
print 'Accuracy = #Correct/#Instances:', classifier.score(X_test_reduced, y_test)
#predictions = classifier.predict(X_test_reduced)
#print classification_report(y_test, predictions)


print '\nTraining the classifier on the unreduced data...'
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
print 'Accuracy = #Correct/#Instances:', classifier.score(X_test, y_test)
#predictions = classifier.predict(X_test)
#print classification_report(y_test, predictions)
