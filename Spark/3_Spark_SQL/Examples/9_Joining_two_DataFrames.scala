val df1 = List(
           ("red", 0, 1, 2, 3),
           ("blue", 4, 5, 6, 7),
           ("yellow", 8, 9, 10, 11),
           ("white", 12, 13, 14, 15)).toDF("color","ball", "pen", "pencil", "paper")
df1.printSchema
df1.show()

val df2 = List(
           ("blue", 0, 1, 2),
           ("green", 3, 4, 5),
           ("white", 6, 7, 8),
           ("yellow", 9, 10, 11)).toDF("color","mug", "pen", "ball")
df2.printSchema
df2.show()

//Inner join
val df_Join = df1.join(df2, df1("color")===df2("color"))
df_Join.show()


//Right outer join
//A right outer join shows all the additional unmatched rows of df2
val df_right_Join = df1.join(df2, df1("color")===df2("color"), "right_outer")
df_right_Join.show()


//Left outer join
//A left outer join shows all the additional unmatched rows of df1
val df_left_Join = df1.join(df2, df1("color")===df2("color"), "left_outer")
df_left_Join.show()

//Operations
val Columns_1 = df1.columns.map(name => df1(name).as(name+"_1"))
val F1 = df1.select(Columns_1 : _*)
F1.show()

val Columns_2 = df2.columns.map(name => df2(name).as(name+"_2"))
val F2 = df2.select(Columns_2 : _*)
F2.show()

val df = F1.join(F2, F1("color_1")=== F2("color_2"))
df.show()

df.withColumn("sum_pen", df("pen_1")+df("pen_2")).show()
