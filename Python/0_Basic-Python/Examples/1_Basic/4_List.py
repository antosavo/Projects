a = [1,2,3,4]
b = [5,6,7,8]

print "a=", a
print "a[1]=", a[1]
print "a[-1]=", a[-1]
print "a[1:3]=", a[1:3]
print "len(a)=", len(a)
print "min(a)=", min(a)
print "max(a)=", max(a)
print "3 in a:", 3 in a
print "5 in a:", 5 in a
print "a+b=", a+b
print "2*a=", 2*a

a.append(42)
print "append 42 : a=", a

a.remove(3)
print "remove 3: a=", a

b = range(10)
print "list in range: b=", b

c = range(3,10)
print "list in range: c=", c

d = range(3,10,2)
print "list in range: d=", d

e = range(10,0,-1)
print "list in range: e=", e
