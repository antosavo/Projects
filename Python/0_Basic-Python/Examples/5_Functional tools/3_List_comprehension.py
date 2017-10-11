vec = [2 , 4 , 6]

a = [3 * x for x in vec ]

print a

b = [3 * x for x in vec if x > 3]

print b

c = [3 * x for x in vec if x < 2]

print c

d = [[ x , x ** 2] for x in vec ]

print d

e = [ x *0.5 for x in range (10)]

print e

f = [ x for x in range (11) if x >5 ]

print f

