import numpy as np

input_file = open("Input_4.dat", "r")
 
y = np.zeros(31) # y data array
x = np.zeros(31) # x data array

i=0

for raw in input_file:
  columns = raw.strip().split()
  x[i] = columns[0]
  y[i]= columns[1]
  i+=1

input_file.close() # close the file

print "i=", i, "len(x)=",len(x) 

out_file = open( "Output_4.dat" , "w" ) # 'w' stands for Writing

for j in range(0,len(x)):
  out_file.write("%lf\t%lf\n" %(x[j],y[j]))

out_file.close() # close the file


  