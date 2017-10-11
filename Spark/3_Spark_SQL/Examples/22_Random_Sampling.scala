val r = scala.util.Random

val df = List.range(0,100).map(i => (i, r.nextDouble)).toDF("range","rand uniform")

df.show(5)

df.sample(true, 0.1).show() //