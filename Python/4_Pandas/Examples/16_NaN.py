import numpy as np
import pandas as pd
#within the pandas library, the calculation of 
#descriptive statistics excludes NaN values implicitly.

frame = pd.DataFrame([[6,np.nan,6],[np.nan,np.nan,np.nan],[2,np.nan,5]],
	index = ['blue','green','red'],
	columns = ['ball','mug','pen'])

print "\nframe with Nan:\n", frame
print "\nframe with no Nan:\n", frame.dropna()
print "\nframe repalce Nan with 0:\n", frame.fillna(0)
print "\nframe replace NaN with different values d:\n", frame.fillna({'ball':1,'mug':0,'pen':99})

