import numpy as np

a = np.array([0,1,0,0,1,1])

def Map(x):
  if x==0 :
    return 1
  else :
    return 0

Map = np.vectorize(Map)

print 'a=', a
print 'not a=', Map(a)

print 'not a=', np.where(a==0,1,0)

print 'map a=', np.vectorize({0:'V', 1:'F'}.get)(a)

def vmap(m,x):
  return np.vectorize(m.get)(x)

print 'map a=', vmap({0:'V', 1:'F'},a)
