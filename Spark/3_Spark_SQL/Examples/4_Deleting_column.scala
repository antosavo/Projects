val L = List((1,"blue","ball",1.2), 
             (2, "green","pen",1.0), 
             (3, "yellow","pencil",0.6),
             (4,"red","paper",0.9),
             (5,"white","mug",1.7)
            )

val df = L.toDF("id","color","object","price")
df.printSchema
df.show()

df.drop("price").show()

df.show()