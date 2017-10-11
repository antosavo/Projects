import scala.io._
import java.io._


val f_out = new FileWriter("My_File.dat")

for(i <- 1 to 5) f_out.write(i+"\t"+(2*i)+"\n")

f_out.close


val f_in = Source fromFile("My_File.dat")

for(line <- f_in.getLines) println(line)

f_in.close