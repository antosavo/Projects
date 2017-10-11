import numpy as np

a = np.zeros(4)

print "a = ", a

o = np.ones(4)

print "o = ", o

N = np.size(a)

print "size a = ", N

print "shape a:", a.shape

b = np.arange(-3.0,5.0,1)

print "b = ", b

c = np.arange(10.0)

print "c = ", c

d = np.linspace(0,10,5)

print "d = ", d

n = np.arange(0,11,1)

print "n = ", n

s = np.sqrt(n)

print "sqrt(n) = ", s

Sb = np.sum(b) 

print "sum(b) = ", Sb

Mb = np.mean(b) 

print "mean(b) = ", Mb

Stdb = np.std(b) 

print "std(b) = ", Stdb

Maxb = np.max(b) 

print "max(b) = ", Maxb

Minb = np.min(b) 

print "min(b) = ", Minb

l = [0,1,2]

np_l = np.array(l) #convert list to np array 

print "l = ", l, "np_l = ", np_l

d = [[0, 1, 2],[4, 5, 6]]

D = np.array(d)

print "D = ", D, "\n", "type(D) = ", type(D)

print "D[0] = ", D[0]

print "D[0][2] = ", D[0][2]

e = np.array([4.5, 2.3, 6.7, 1.2, 1.8, 5.5])

print "e = ", e

E = np.sort(e)

print "sorted(e) = ", E

np.random.seed(123)

x = np.random.uniform()

print "uniform random number = ", x

y = np.random.uniform(-1,1,10)

print "uniform random np array = ", y

#np.random.uniform(0,1,(4,4)) #4x4 matrix
#np.random.randn(1000,3) # 1000x3 normal distributed
#np.random.rand(1000,3) # 1000x3 uniform distributed
#np.random.randint(0,10,3) #0 to 10, 3 samples

mean = 0
sigma = 2
Number = 10

sample = np.random.normal(mean, sigma, Number)

print "normal random np array = ", sample

print "mean = ", np.mean(sample), "std = ", np.std(sample)
