import numpy as np
import pandas as pd

df = pd.read_csv('data_02.csv', header=None)
print "df:\n", df

df2 = pd.read_csv('data_02.csv', skiprows=[2], header=None)
print "df skipped row 2:\n", df2

df3 = pd.read_csv('data_02.csv', nrows=3, header=None)
print "df read 3 rows:\n", df3

df1 = pd.read_csv('data_02.csv', chunksize=3, header=None)
for chunk in df1:
  print "chunk:\n", chunk
