import numpy as np
import pandas as pd
import pylab as plt

df = pd.DataFrame(np.arange(25).reshape(5,5))
print "df:\n", df

new_order = np.random.permutation(5)

print "new_order:\n", new_order

print "df new order:\n", df.take(new_order)

print "df take some rows:\n", df.take([3,4,2])
