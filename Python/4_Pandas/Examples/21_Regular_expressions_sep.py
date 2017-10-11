import numpy as np
import pandas as pd

df = pd.read_csv('RE_01.txt',sep='\s*')# \s* stands for space or tab character
print "df1:\n", df

df2 = pd.read_csv('RE_02.txt',sep='\D*', header=None)# \D* means non-digit character
print "df2:\n", df2

df3 = pd.read_csv('RE_03.txt',sep=',', skiprows=[0,1,3,6])
print "skip rows df3:\n", df3