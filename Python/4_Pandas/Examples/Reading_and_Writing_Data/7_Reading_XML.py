import numpy as np
import pandas as pd
from lxml import objectify

xml = objectify.parse('books.xml')
print "xml:\n", xml

root = xml.getroot()
#Now that the root of the structure has been defined,
#you can access the various nodes of the tree.

N1 = len(root.getchildren())
print "\nNumber of elements at Level 1 = ", N1

N2 = len(root.getchildren()[0].getchildren())
print "\nNumber of elements at Level 2 = ", N2

print "\nLevel 1 Tags:"
for i in range(0,N1):
  print root.getchildren()[i].tag

print "\nLevel 2 Tags:"
for i in range(0,N2):
  print root.getchildren()[0].getchildren()[i].tag

print "\nBook 0 Text:"
for i in range(0,N2):
  print root.getchildren()[0].getchildren()[i].text

print "\nBook 1 Text:"
for i in range(0,N2):
  print root.getchildren()[1].getchildren()[i].text

print "\nAuthor 0:", root.Book.Author
print "PublishDate 0:", root.Book.PublishDate

#Create df
column_names = []
for i in range(0,N2):
  Tag = root.getchildren()[0].getchildren()[i].tag
  column_names.append(Tag)
print "column_names:", column_names

row0 = []
for i in range(0,N2):
  Text = root.getchildren()[0].getchildren()[i].text
  row0.append(Text)
print "row0:", row0

row1 = []
for i in range(0,N2):
  Text = root.getchildren()[1].getchildren()[i].text
  row1.append(Text)
print "row1:", row1

df = pd.DataFrame([row0,row1], columns = column_names)
print "df:\n", df









'''
<?xml version="1.0"?>
<Catalog>
 <Book id="ISBN9872122367564">
  <Author>Ross, Mark</Author>
  <Title>XML Cookbook</Title>
  <Genre>Computer</Genre>
  <Price>23.56</Price>
  <PublishDate>2014-22-01</PublishDate>
 </Book>
 <Book id="ISBN9872122367564">
  <Author>Bracket, Barbara</Author>
  <Title>XML for Dummies</Title>
  <Genre>Computer</Genre>
  <Price>35.95</Price>
  <PublishDate>2014-12-16</PublishDate>
 </Book>
</Catalog>
'''