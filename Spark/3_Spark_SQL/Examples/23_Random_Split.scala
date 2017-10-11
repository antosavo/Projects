val r = scala.util.Random

val df = List.range(0,100).map(i => (i, r.nextDouble)).toDF("range","rand uniform")

df.show(5)

val dfArray = df.randomSplit(Array(0.6, 0.2, 0.2))

println("Elements in df_0: " + dfArray(0).count)
dfArray(0).show(5)

println("Elements in df_1: " + dfArray(1).count)
dfArray(1).show(5)

println("Elements in df_2: " + dfArray(2).count)
dfArray(2).show(5)