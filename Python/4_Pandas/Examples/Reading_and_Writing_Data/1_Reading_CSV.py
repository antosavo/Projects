import numpy as np
import pandas as pd

csvframe = pd.read_csv('data_01.csv')
print "csvframe:\n", csvframe

table = pd.read_table('data_01.csv', sep=',')
print "table:\n", table

csvframe2 = pd.read_csv('data_02.csv')
print "csvframe2:\n", csvframe2

csvframe2 = pd.read_csv('data_02.csv', header=None)
print "csvframe2 assigned name:\n", csvframe2

csvframe2 = pd.read_csv('data_02.csv', names=['white','red','blue','green','animal'])
print "csvframe2 assigned name2:\n", csvframe2

csvframe3 = pd.read_csv('data_03.csv', index_col=['color','status'])
print "csvframe3 with a hierarchical structure:\n", csvframe3