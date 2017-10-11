import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import seaborn as sbn

df = pd.read_excel('Boston.xls')

cols = df.columns.values

sbn.heatmap(df.corr(),cbar=True,annot=True,square=True,fmt='.1f',annot_kws={'size': 10},yticklabels=cols,xticklabels=cols)
plt.savefig('correlation_matrix.png')
plt.show()

sbn.pairplot(df,size=1, plot_kws={'s': 5})
plt.savefig('scatter_matrix.png')
plt.show()