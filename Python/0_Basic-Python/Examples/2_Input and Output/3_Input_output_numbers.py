input_file = open( "Input_3.dat" , "r" ) # 'r' stands for reading
x,y = input_file.read().strip().split()

x = float(x)
y = float(y)

input_file.close() # close the file

print x, type(x)
print y, type(y)

out_file = open( "Output_3.dat" , "w" ) # 'w' stands for Writing
out_file.write("x=%lf\ty=%lf\n" %(x,y))
out_file.close() # close the file
