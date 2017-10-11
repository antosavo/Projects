/*flatMap generates a collection for each element in the original collection.*/

val line = "Scala is fun"

println("line = "+line)

val SingleSpace = " "
val words = line.split(SingleSpace)

println("words = "+words.toList)


val ListOfList = words.map(_.toList)

println("ListOfList = " +ListOfList.toList)


val ListOfChars = words.flatMap(_.toList)

println("ListOfChars = " +ListOfChars.toList)
