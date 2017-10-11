import pandas as pd
import matplotlib.pylab as plt

data_frame= pd.read_csv('winequality-red.csv', sep=';')
print "\nDescription:\n\n", data_frame.describe() #It describes the data frame
print "\nCorrelation:\n\n", data_frame.corr() #It founds the correlations
print "\nShape:", data_frame.shape #It founds the shape
print "\nNumber of Columns:", data_frame.shape[1]

name_0 = data_frame.columns[0]
print "\nName column 0:", name_0

N = data_frame.shape[1]

name_all = data_frame.columns[0:N]
print "\nName all columns:", list(name_all)

plt.scatter(data_frame['alcohol'], data_frame['quality'])
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.title('Alcohol Against Quality')
plt.savefig('4_Alcohol_Against_Quality.png')
plt.show()

