import numpy as np
import pandas as pd

table = pd.read_csv('Input_1.dat', sep=' ', header=None)

print "table:\n", table

table.to_csv('Output_5.dat',  sep=' ', index=None, header=None)