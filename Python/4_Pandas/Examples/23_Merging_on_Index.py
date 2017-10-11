import numpy as np
import pandas as pd

frame1 = pd.DataFrame( {'id':['ball','pencil','pen','mug','ashtray'],
	'color': ['white','red','red','black','green'],
	'brand': ['OMG','ABC','ABC','POD','POD']})
print "frame1:\n", frame1

frame2 = pd.DataFrame( {'id':['pencil','pencil','ball','pen'],
	'brand': ['OMG','POD','ABC','POD']})
print "frame2:\n", frame2

print "merged on index:\n", pd.merge(frame1,frame2,right_index=True, left_index=True)

frame2.columns = ['brand2','id2']
print "merge using join:\n", frame1.join(frame2)








