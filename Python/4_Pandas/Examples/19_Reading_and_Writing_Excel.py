import numpy as np
import pandas as pd

df = pd.read_excel('data.xls')
print "df:\n", df

df2 = pd.read_excel('data.xls','Sheet2')
print "df2:\n", df2

df3 = pd.read_excel('data.xls',1)
print "df3:\n", df3
#np.random.random((4,4))

df4 = pd.DataFrame(np.random.uniform(0,1,(4,4)),
	index = ['exp1','exp2','exp3','exp4'],
	columns = ['Jan2015','Fab2015','Mar2015','Apr2005'])
print "df4:\n", df4

df4.to_excel('data2.xls')
