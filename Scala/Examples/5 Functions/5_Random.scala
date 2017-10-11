val r = scala.util.Random

//Uniform distribution 0 to 1
val Uniform = Array.range(0,10).map(i => r.nextDouble)
println("Uniform distribution:")
Uniform.foreach(println)

//Normal distribution avg 0 stddev 1
val Normal = Array.range(0,10).map(i => r.nextGaussian)
println("Normal distribution:")
Normal.foreach(println)


