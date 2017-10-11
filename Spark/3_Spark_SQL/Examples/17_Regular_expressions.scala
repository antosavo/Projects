case class Color(white: String, red: String, blue: String, green: String)

val rowsRDD = sc.textFile("re_01.txt")

val header = rowsRDD.first()

val rowsRDD2 = rowsRDD.filter(row => row != header )

val ColorRDD = rowsRDD2.
	map{row => row.split("\\s+")}.// \\s+ stands for space or tab character
	map{col => Color(col(0), col(1), col(2), col(3))}

val ColorDF = ColorRDD.toDF()

ColorDF.show()


val rowsRDD = sc.textFile("re_02.txt")

val ColorRDD = rowsRDD.
	map{row => row.split("\\D+")}.// \\D+ means non-digit character
	map{col => Color(col(0), col(1), col(2), col(3))}

val ColorDF = ColorRDD.toDF()

ColorDF.show()


val rowsRDD = sc.textFile("re_03.txt")

val allrows = rowsRDD.collect()

val rowsRDD2 = rowsRDD.filter(row => row != allrows(0) && row != allrows(3)  ) //skip rows 0 and 3

val ColorRDD = rowsRDD2.
	map{row => row.split(",")}.// \\s+ stands for space or tab character
	map{col => Color(col(0), col(1), col(2), col(3))}

val ColorDF = ColorRDD.toDF()

ColorDF.show()


//df3 = pd.read_csv('RE_03.txt',sep=',', skiprows=[0,3])
