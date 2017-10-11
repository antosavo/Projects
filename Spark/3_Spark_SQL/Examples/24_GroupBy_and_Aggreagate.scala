val L = List((1,"blue","ball",1.2), 
             (2, "green","pen",1.0), 
             (3, "red","pencil",0.6),
             (4,"green","paper",0.9),
             (5,"red","mug",1.7)
            )

val df = L.toDF("id","color","object","price")
df.printSchema
df.show()

df.groupBy("color").sum().show()

df.groupBy("color").agg(max("price"), min("price"), mean("price"), sum(sin("id"))).show()

