val df = List(
	(0,"white",2),
	(1,"white",1),
	(2,"red",3),
	(3,"red",3),
	(4,"white",2)
	).toDF("id", "color", "value")

df.show()

df.select("color","value").dropDuplicates().show()

df.dropDuplicates(List("color","value")).show()