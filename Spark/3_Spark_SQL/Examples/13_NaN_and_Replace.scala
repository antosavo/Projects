val df = List(
    ("blue", 6.0, 6.0, 6.0),
    ("green", Double.NaN, Double.NaN, Double.NaN),
    ("red", 2.0, Double.NaN, 5.0)
    ).toDF("index","ball","mug","pen")
df.show()

df.na.drop().show()

df.na.fill(0).show()

df.na.replace("*", Map(6.0 -> 7.0, 2.0 -> 3.5)).show()