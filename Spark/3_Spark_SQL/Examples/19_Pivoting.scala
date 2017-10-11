val df= List(
	("white", "ball", 0.2),
	("white", "pen", 0.9),
	("white", "mug", 0.9),
	("white", "ball", 0.4),
	("white", "pen", 0.8),
	("white", "mug", 0.1),
	("red", "ball", 0.8),
	("red", "pen", 0.1),
	("red", "mug", 0.3),
	("red", "ball", 0.7),
	("red", "pen", 0.5),
	("red", "mug", 0.2),
	("black", "ball", 0.8),
	("black", "pen", 1.0),
	("black", "mug", 0.5),
	("black", "ball", 0.6),
	("black", "pen", 0.0),
	("black", "mug", 0.3)
	).toDF("color", "item", "value") 
df.show()

df.groupBy("color").pivot("item").mean().show()
df.groupBy("color").pivot("item").agg(sum(df("value")+1)).show()