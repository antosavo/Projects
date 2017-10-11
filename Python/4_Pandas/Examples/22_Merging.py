import numpy as np
import pandas as pd

frame1 = pd.DataFrame( {'id':['ball','pencil','pen','mug','ashtray'],
	'price': [12.33,11.44,33.21,13.23,33.62]})
print "frame1:\n", frame1

frame2 = pd.DataFrame( {'id':['pencil','pencil','ball','pen'],
	'color': ['white','red','red','black']})
print "frame2:\n", frame2

print "merge frame 1 and 2 on id:\n", pd.merge(frame1,frame2, on = 'id')
#The returned DataFrame consists of all rows that have an ID in common
#between the two DataFeame.

#Rename columns
frame2.columns = ['color','sid']
print "frame2 new column names:\n", frame2

#merge DataFrames in which the key columns do not have the same name. 
print "merge frame 1 and 2 left on='id' and right on='sid':\n", pd.merge(frame1, frame2, left_on='id', right_on='sid')


#By default, the merge function performs an inner join, the keys in the result are the result of an intersection.
#The outer join produces the union of all keys.
frame2.columns = ['color','id']
print "merge frame 1 and 2 inner on id:\n", pd.merge(frame1, frame2, on='id')
print "merge frame 1 and 2 outer on id:\n", pd.merge(frame1,frame2, on='id', how='outer')
print "merge frame 1 and 2 left on id:\n", pd.merge(frame1,frame2, on='id', how='left')
print "merge frame 1 and 2 right on id:\n", pd.merge(frame1,frame2, on='id', how='right')




