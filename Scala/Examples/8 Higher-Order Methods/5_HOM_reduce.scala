
val L = List(2, 4, 6, 8, 10)
println("L = " +L)

val sum = L.reduce( (x,y) => x + y )
println("Lsum = " +sum)

val product = L.reduce( (x,y) => x * y )
println("Lproduct = " +product)

val max = L.reduce( (x,y) => if (x > y) x else y)
println("Lmax = " +max)

val min = L.reduce( (x,y) => if (x < y) x else y)
println("Lmin = " +min)

val words = "Scala is fun".split(" ")
println("word = " +words.toList)

val longestWord = words.reduce( (w1, w2) => if(w1.length > w2.length) w1 else w2)
println("longestWord = " +longestWord)


