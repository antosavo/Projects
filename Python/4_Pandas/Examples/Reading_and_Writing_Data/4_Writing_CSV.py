import numpy as np
import pandas as pd

df = pd.read_csv('data_01.csv')
print "df:\n", df

df.to_csv('data_7.csv') 
df.to_csv('data_8.csv', index=False, header=False) 

df3 = pd.DataFrame([[6,np.nan,6],[np.nan,np.nan,np.nan],[2,np.nan,5]],
	index = ['blue','green','red'],
	columns = ['ball','mug','pen'])

print "\nframe with Nan:\n", df3

# NaN values present in a datastructure are shown as empty fields in the file
df3.to_csv('data_9.cvs') 
#you can replace this empty field with a value to your liking using the na_rep
df3.to_csv('data_10.cvs', na_rep ='NaN')
