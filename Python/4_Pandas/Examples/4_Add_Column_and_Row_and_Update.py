import numpy as np
import pandas as pd 

data = {'color' : ['blue','green','yellow','red','white'],
	'object' : ['ball','pen','pencil','paper','mug'],
	'price' : [1.2,1.0,0.6,0.9,1.7]}

df = pd.DataFrame(data)
print "\nData Frame :\n", df

df['new'] = 12 #Add a new column
print "\nData Frame with new column:\n", df

df['new'] = [3.0,1.3,2.2,0.8,1.1] #Update 'new'
print "\nData Frame with new column:\n", df

df['new'] = np.arange(5) #Update 'new'
print "\nData Frame with new column:\n", df

df['price'][2] = 3.3
print "\nData Frame with new column:\n", df


print "\nData Frame with new row:\n", df.append({'color' : 'gray',
                                                 'object' : 'ball',
                                                 'price' : 3.2, 
                                                 'new' : 7.5},ignore_index=True)
