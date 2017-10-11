import java.io._

/*Write*/
val f_out = new FileWriter("My_File.dat")

f_out.write("Hello Scala")

f_out.close()

/*Read*/
val f_in = new FileReader("My_File.dat")

var a = new Array[Char](15)

f_in.read(a)

println(a.mkString)

f_in.close()