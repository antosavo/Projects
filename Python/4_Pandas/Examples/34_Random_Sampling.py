import numpy as np
import pandas as pd
import pylab as plt

df = pd.DataFrame(np.arange(25).reshape(5,5))
print "df:\n", df

sample = np.random.randint(0, len(df), size=3)
print "sample:\n", sample

print "take sample:\n", df.take(sample)

