try:
  f = open("filenamethatdoesnotexist","r")
except IOError:
  print "The file does not exist!!!"