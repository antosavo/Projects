#term frequency-inverse document frequency (tf-idf)
#When we are analyzing text data, we often encounter frequent words that occur across
#multiple documents. Those frequently occurring words typically
#don't contain useful or discriminatory information.
#The tf-idf can be defined as the product of the term frequency and the inverse document frequency:

#tf-idf = tf*idf 

#tf = f/Norm

#the inverse document frequency idf can be calculated as:

#idf(t,d)= 1 + log[(1+nd)/(1+df(d,t))]

#where nd is the total number of documents, and df(d,t) is the number of documents d 
#that contain the term t.

#Note that adding the constant 1 to the denominator is  optional and serves the purpose 
#of assigning a non-zero value to terms that occur in all training samples; 
#the log is used to ensure that low document frequencies are not given too much weight.
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances

vectorizer = TfidfVectorizer(stop_words='english')
#stop words remuves words such as the, a, and an; 
#auxiliary verbs such as do, be, and will; 
#and prepositions such as on, around, and beneath;

docs = np.array([
	'The dog ate a sandwich and I ate a sandwich',
	'The wizard transfigured a sandwich'
	])

bag = vectorizer.fit_transform(docs).toarray()

print 'bag:\n', bag
print 'Vocabulary:', vectorizer.vocabulary_
print 'Names:', vectorizer.get_feature_names()

#print 'Distance between 1st and 2nd documents:', euclidean_distances(bag[0], bag[1])