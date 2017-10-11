import numpy as np
import pandas as pd
import pylab as plt

frame = pd.DataFrame({  'color': ['white','red','green','red','green'],
			'object': ['pen','pencil','pencil','ashtray','pen'],
			'price1' : [5.56,4.20,1.30,0.56,2.75],
			'price2' : [4.75,4.12,1.60,0.75,3.15]})
print "\nframe:\n", frame

#Group By 
print "\ngroups by color:\n", frame['price1'].groupby(frame['color']).groups
print "\nmean price 1 by color:\n", frame['price1'].groupby(frame['color']).mean()
print "\nsum price 1 by color:\n", frame['price1'].groupby(frame['color']).sum()

#Hierarchical Grouping
print "\nsum price 1 by color and object:\n", frame['price1'].groupby([frame['color'],frame['object']]).sum()

print "\nmean price 1 and 2 by color:\n", frame[['price1','price2']].groupby(frame['color']).mean().add_prefix('mean_')


