import numpy as np
from stemming.porter2 import stem
from sklearn.feature_extraction.text import CountVectorizer


print 'stem(run):', stem('run')
print 'stem(running):', stem('running')

#####

docs = [
	'The sun is shining and thus it shines',
	'The weather is sweet',
	'The sun is shining and the weather is sweet']

print 'docs:\n', docs

def tokenizer_porter(doc):
  return [stem(word) for word in doc.split()]

print 'tokenized docs[0]:\n', tokenizer_porter(docs[0])

vectorizer = CountVectorizer(stop_words='english', tokenizer = tokenizer_porter)

bag = vectorizer.fit_transform(docs).toarray()

print 'bag:\n', bag
print 'Names:', vectorizer.get_feature_names()
