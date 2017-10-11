import scala.tools.nsc.io._
import scala.io.Source._

val s_out = File("My_File.dat")

s_out.writeAll("Hello world")

val s_in = fromFile("My_File.dat").mkString

println(s_in)