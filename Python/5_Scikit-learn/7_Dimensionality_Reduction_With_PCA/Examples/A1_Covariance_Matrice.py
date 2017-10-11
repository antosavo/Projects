#A covariance matrix describes the covariance values between each pair 
#of dimensions in a data set.
import numpy as np

X = [[2, 0, -1.4],
     [2.2, 0.2, -1.5],
     [2.4, 0.1, -1],
     [1.9, 0, -1.2]]

print np.cov(np.array(X).T)


x = np.array([6, 8, 10, 14, 18])
y = np.array([7, 9, 13, 17.5, 18])

print "Mean(x) =", np.mean(x)
print "Variance(x) =", np.var(x, ddof=1) #ddof is to divide by n-1 instead of n, sum((x-<x>)**2)/(n-1)
print "std(x) = sqrt(var(x))=", np.std(x, ddof=1)
print "Covariance(x,y) =", np.cov(x, y)[0][1] # sum((x_i-<x>)*(y_i-<y>))/(n-1)
print "Cov =", np.sum((x-np.mean(x))*(y-np.mean(y)))/4
print "Correlation(x,y) =", np.corrcoef(x,y) #sum((x_i-<x>)*(y_i-<y>))/sqrt(sum((x_i-<x>)**2)*sum((y_i-<y>)**2))

Cov = np.cov(x, y)
print "Cor =", Cov[0][1]/(np.sqrt(Cov[0][0])*np.sqrt(Cov[1][1]))
