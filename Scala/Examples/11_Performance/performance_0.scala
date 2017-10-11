def timed(op: => Unit) = { val start = System.nanoTime; op;
(System.nanoTime - start) / 1e9 }

val a = Array.fill(10000)(1)
val v = Vector.fill(10000)(1)
val l = List.fill(10000)(1)

println("Time List for:")
println(timed { var t = 0; for (i <- 0 until l.length - 1) yield t +=
l(i) + l(i + 1) })

println("Time List while:")
println(timed { var t = 0; var i = 0; while (i < l.length - 1) { t +=
l(i) + l(i + 1); i += 1 } })

println("Time Vector for:")
println(timed { var t = 0; for (i <- 0 until v.length - 1) yield t +=
v(i) + v(i + 1) })

println("Time Vector while:")
println(timed { var t = 0; var i = 0; while (i < v.length - 1) { t +=
v(i) + v(i + 1); i += 1 } })

println("Time Array for:")
println(timed { var t = 0; for (i <- 0 until a.length - 1) yield t +=
a(i) + a(i + 1) })

println("Time Array while:")
println(timed { var t = 0; var i = 0; while (i < a.length - 1) { t +=
a(i) + a(i + 1); i += 1 } })
