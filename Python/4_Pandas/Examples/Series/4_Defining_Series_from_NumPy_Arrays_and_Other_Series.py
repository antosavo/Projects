# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

s = pd.Series([12,-4,7,9], index=['a','b','c','d']) #assigned index

print "\nSeries s:\n", s


arr = np.array([1,2,3,4])

s2 = pd.Series(arr)

print "\nSeries s2:\n", s2 

arr[2] = -2
#t the values contained within the
#NumPy array or the original Series are not copied, but are passed by reference. 

print "\nSeries s2:\n", s2 


s3 = pd.Series(s)

print "\nSeries s3:\n", s 