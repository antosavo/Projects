#Hashing trick works by applying a hash function to the features and using their hash values 
#as indices directly, rather than looking the indices up in an associative array.

from sklearn.feature_extraction.text import HashingVectorizer
import numpy as np

#corpus = ['the', 'ate', 'bacon', 'cat']

corpus = np.array([
	'The dog ate a sandwich and I ate a sandwich',
	'The wizard transfigured a sandwich'
	])

vectorizer = HashingVectorizer(stop_words='english', n_features=6)

#n_features is an optional keyword argument. Its default value,
#2^20 , is adequate for most problems; it is set to 6 here so that the matrix will be small
#enough to print and still display all of the nonzero features.

print vectorizer.transform(corpus).todense()