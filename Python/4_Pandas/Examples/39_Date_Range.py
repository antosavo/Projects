import numpy as np
import pandas as pd
import pylab as plt

#date range
temp = pd.date_range('1/1/2015', periods=10, freq= '15min')#freq= 's','min','H','D','W','M','A'

timetable = pd.DataFrame( {'date': temp, 
		'value1' : np.random.rand(10),
		'value2' : np.random.rand(10)})

print "timetable:\n", timetable






