#Bag-of-words model allows us to represent text as numerical feature vectors. 
#The idea behind the bag-of-words can be summarized as follows:
#1. We create a vocabulary of unique words from the entire set of documents.
#2. We construct a feature vector from each document that contains the counts of
#occurring words.
#Since the unique words in each document represent only a small subset of all the
#words in the bag-of-words vocabulary, the feature vectors will consist of mostly
#zeros, which is why we call them sparse.
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

vectorizer = CountVectorizer(stop_words='english')
#stop words remuves words such as the, a, and an; 
#auxiliary verbs such as do, be, and will;
#and prepositions such as on, around, and beneath;

docs = np.array([
	'The sun is shining',
	'The weather is sweet',
	'The sun is shining and the weather is sweet'])

bag = vectorizer.fit_transform(docs).toarray()

print 'bag:\n', bag
print 'Vocabulary:', vectorizer.vocabulary_
print 'Names:', vectorizer.get_feature_names()

#By calling the fit_transform method on CountVectorizer, we just constructed
#the vocabulary of the bag-of-words model and transformed the three sentences 
#into sparse feature vectors.
#Each index position in the feature vectors shown here corresponds to the integer
#values that are stored as dictionary items in the CountVectorizer vocabulary. 
#Those values in the feature vectors are also called the raw term frequencies.

print 'Distance between 1st and 2nd documents:', euclidean_distances(bag[0], bag[1])
print 'Distance between 1st and 3rd documents:', euclidean_distances(bag[0], bag[2])
print 'Distance between 2nd and 3rd documents:', euclidean_distances(bag[1], bag[2])

print 'Distance between 2nd and 3rd documents B:', np.sqrt((bag[1]-bag[2]).dot(bag[1]-bag[2]))
print 'Distance between 2nd and 3rd documents C:', np.linalg.norm(bag[1]-bag[2])

