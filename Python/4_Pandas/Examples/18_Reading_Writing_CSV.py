import numpy as np
import pandas as pd

#Reading CSV

df = pd.read_csv('data_01.csv')
print "df:\n", df

table = pd.read_csv('table.txt', sep='\t')
print "table:\n", table

df2 = pd.read_csv('data_02.csv', header=None)
print "df2 assigned number name:\n", df2

df2 = pd.read_csv('data_02.csv', names=['white','red','blue','green','animal'])
print "df2 assigned custom name:\n", df2

df3 = pd.read_csv('data_03.csv', index_col=['color','status'])
print "df3 with a hierarchical structure:\n", df3

#Writing CSV

df.to_csv('data_04.csv', sep = '\t', index=None, header=None)

#Writing CSV with nan

df4 = pd.DataFrame([[6,np.nan,6],[np.nan,np.nan,np.nan],[2,np.nan,5]],
	index = ['blue','green','red'],
	columns = ['ball','mug','pen'])

print "\nframe with Nan:\n", df4

# NaN values present in a datastructure are shown as empty fields in the file
df4.to_csv('data_05.cvs') 

#you can replace this empty field with a value to your liking using the na_rep
df4.to_csv('data_06.cvs', na_rep ='NaN')