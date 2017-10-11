import numpy as np
import pandas as pd
import pylab as plt

text = '16 Bolton Avenue , Boston'
print "text:\n", text

print "splitted text:\n", text.split(',')

for s in text.split(','):
  print s.strip()

trimmed = [s.strip() for s in text.split(',')]
print "trimed text (no space character):\n", trimmed 

address, city = [s.strip() for s in text.split(',')]
print "address:", address
print "city:", city

print "address + ',' + city:", address + ',' + city

strings = ['A+','A','A-','B','BB','BBB','C+']
print "strings:\n", strings
print "join strings:\n", ';'.join(strings)

print "'Boston' in text:",  'Boston' in text
print "'Boston' at:", text.index('Boston')
print "'Boston' at:", text.find('Boston')

print "'new' at:", text.find('new')
print "'Avenue' at:", text.find('Avenue')
#print "'new' at:", text.index('new')

print "count 'e':", text.count('e')
print "count 'Avenue':", text.count('Avenue')

print "replace 'Avenue' => 'Street':\n", text.replace('Avenue','Street')
print "replace '1' => '':\n", text.replace('1','')



 

