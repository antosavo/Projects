val df1 = List(
           ("red", 0, 1, 2, 3),
           ("blue", 3, 9, 5, 8),
           ("yellow", 8, 9, 10, 11),
           ("white", 12, 13, 14, 15)).toDF("color","ball", "pen", "pencil", "paper")
df1.show()

val df2 = List(
           ("red", 1, 4, 3, 6),
           ("blue", 4, 5, 6, 1),
           ("yellow", 3, 3, 1, 5),
           ("white", 4, 1, 6, 4)).toDF("color","ball", "pen", "pencil", "paper")
df2.show()


//Correlation
val F1 = df1.select(col("color").as("color_1"), col("ball").as("ball_1"))
val F2 = df2.select(col("color").as("color_2"), col("ball").as("ball_2"))

val df = F1.join(F2, F1("color_1")===F2("color_2"))
df.show()

df.stat.corr("ball_1", "ball_2") // sum((x_i-<x>)*(y_i-<y>))

