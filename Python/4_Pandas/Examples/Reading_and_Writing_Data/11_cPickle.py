import numpy as np
import pandas as pd
import cPickle as pickle

data = { 'color': ['white','red'], 'value': [5, 7]} # dict object.

#serialization of the data object through the dumps() function 
pickled_data = pickle.dumps(data)
print "pickled data:\n", pickled_data

#Once you have serialized data, they can easily be written on a file.
nframe = pickle.loads(pickled_data)
print "nframe:\n", nframe

#Pickling with pandas
frame = pd.DataFrame(np.arange(16).reshape(4,4), index = ['up','down','left','right'])
frame.to_pickle('frame.pkl')

df = pd.read_pickle('frame.pkl')
print "df:\n", df



