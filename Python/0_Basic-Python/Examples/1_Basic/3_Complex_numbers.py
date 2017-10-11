import cmath

x = 1 + 3j

print "x=", x

print "|x|=", abs(x) # computes the absolute value

print "Im(x)", x.imag

print "Re(x)", x.real

print "x*=", x.conjugate()

print "|x|=", cmath.sqrt(x*x.conjugate())

print "3x=", 3 * x
