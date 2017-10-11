case class Employee(id: Int, studentName: String, phone: String, email: String)

val rowsRDD = sc.textFile("EmployeeData.csv")

val employeesRDD = rowsRDD.
	map{row => row.split(",")}.
	map{col => Employee(col(0).toInt, col(1), col(2), col(3))}

val employeesDF = employeesRDD.toDF()

employeesDF.show(10)