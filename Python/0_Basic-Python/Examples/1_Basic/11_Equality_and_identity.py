x = [0,1,2]

y = x

print "x == y ? : ", x == y
print "x is y ? : ", x is y
print "id(x) = ", id(x)
print "id(y) = ", id(y)

x[0] = 100

print "x = ", x
print "y = ", y, ", y is modified"

z = x[:]

print "x == z ? : ", x == z
print "x is z ? : ", x is z
print "id(x) = ", id(x)
print "id(z) = ", id(z)

x[0] = 200

print "x = ", x
print "z = ", z, ", z is not modified"