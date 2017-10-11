import breeze.linalg._
import breeze.numerics._ //for functions sin, log
import breeze.stats._ //for stsistics

val v = linspace(0, 4, 5)

println("v = " + v)

println("<v> = " + mean(v) ) //this needs a vector of Double
println("stddev(v) = " + stddev(v) ) //this needs a vector of Double
println("max(v) = " + max(v) )
println("min(v) = " + min(v) )
println("sum(v) = " + sum(v) )
println("sin(v) = " + sin(v) )
println("log(v) = " + log(v) )
println("sqrt(v) = " + sqrt(v) )
println("pow(v,2.0) = " + pow(v,2.0) )

