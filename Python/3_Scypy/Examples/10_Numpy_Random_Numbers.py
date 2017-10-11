import numpy as np

print "3 random numbers 0 to 10 = ", np.random.randint(0,10,3)

np.random.seed(123)

mean = 0
sigma = 2
Number = 5

sample = np.random.normal(mean, sigma, Number)

print "normal random array : \n", sample

print "mean = ", np.mean(sample)

print "std = ", np.std(sample)

print "min = ", np.min(sample)

print "max = ", np.max(sample)


print "uniform random number : ", np.random.uniform()

print "uniform random array :\n", np.random.uniform(-1,1,5)

print "uniform random matrix 4x4 :\n", np.random.uniform(-1,1,(4,4))

print "uniform random matrix 4x4 from 0 to 1:\n", np.random.rand(4,4)

print "normal random matrix 4x4 :\n", np.random.normal(mean, sigma, (4,4))

print "normal random matrix 4x4 mean 0 sigma 1:\n", np.random.randn(4,4)


