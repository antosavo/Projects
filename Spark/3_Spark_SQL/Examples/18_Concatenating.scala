val r = scala.util.Random

val df1 = List.range(0,5).map(i => (i, r.nextDouble, r.nextDouble, r.nextDouble)).toDF("id", "A", "B", "C")
df1.show()

val df2 = List.range(5,10).map(i => (i, r.nextDouble, r.nextDouble, r.nextDouble)).toDF("id", "A", "B", "C")
df2.show()

val df_1_2 = df1.unionAll(df2)
df_1_2.show()