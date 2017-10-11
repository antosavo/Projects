import java.io._

/*Write*/
val f_out = new FileWriter("Data.dat")

for(i <- 1 to 5) f_out.write(i + "\t" + (2*i) + "\n")

f_out.close()

/*Read*/
val f_in = new FileReader("Data.dat")

var a = new Array[Char](20)

f_in.read(a)

println(a.mkString)

f_in.close()

/*Splitting*/

val elements = a.mkString.split("\\W+").toArray // \W+ is to skip not alphanumeric char

var x = new Array[String](5)
var y = new Array[String](5)

for(i <- 0 to 4)
{
  x(i) = elements(2*i)
  y(i) = elements(2*i+1)
}

println("x = " + x.toList)
println("y = " + y.toList)

f_in.close()