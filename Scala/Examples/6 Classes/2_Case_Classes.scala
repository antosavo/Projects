case class Car(mk: String, ml: String, cr: String) 
{
	val make = mk
	val model = ml
	var color = cr //It is variable

	def repaint(newColor: String) = 
	{
	color = newColor
	}

}

val mustang = Car("Ford", "Mustang", "Red") //To create a new istance, no new is needed

println("Make:" + mustang.make + "\nModel:" + mustang.model + "\nColor:" + mustang.color)

mustang.repaint("Yellow") 

println("\nMake:" + mustang.make + "\nModel:" + mustang.model + "\nColor:" + mustang.color)


