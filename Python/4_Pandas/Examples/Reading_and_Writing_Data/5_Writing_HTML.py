import numpy as np
import pandas as pd


frame = pd.DataFrame(np.arange(4).reshape(2,2))
print "frame to html:\n", frame.to_html()

frame2 = pd.DataFrame( np.random.random((4,4)),
	index = ['white','black','red','blue'],
	columns = ['up','down','right','left'])

print "frame2:\n", frame2

s = ['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame2.to_html())
s.append('</BODY></HTML>')
html = ''.join(s)

html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()


