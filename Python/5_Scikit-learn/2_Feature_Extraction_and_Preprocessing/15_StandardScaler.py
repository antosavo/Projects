import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale

df = pd.read_csv('winequality-red.csv', sep=';')

Names = df.columns.values[0:-1]
#print "\nNames of all columns except the last one:\n", Names

x = df[Names]#the last column is the quality that is the y parameter, [0:-1] means all but not the last
y = df['quality']

scaler = StandardScaler()

print "original mean x:\n", x.mean(axis=0)
print "original std x:\n", x.std(axis=0)

x_scaled = scaler.fit_transform(x)

print "mean x scaled:\n", x_scaled.mean(axis=0).astype(int)
print "std x scaled:\n", x_scaled.std(axis=0)

x_rescaled = scaler.inverse_transform(x_scaled)

print "mean x rescaled:\n", x_rescaled.mean(axis=0)
print "std x rescaled:\n", x_rescaled.std(axis=0)

x_scaled2 = scale(x)

print "mean x scaled2:\n", x_scaled2.mean(axis=0).astype(int)
print "std x scaled2:\n", x_scaled2.std(axis=0)
