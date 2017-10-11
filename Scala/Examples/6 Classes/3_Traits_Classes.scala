trait Shape 
{
  def area(): Int
}

class Square(length: Int) extends Shape 
{
  def area = length * length
}

class Rectangle(length: Int, width: Int) extends Shape 
{
  def area = length * width
}


val shape1 = new Square(10)

println("Square Area = " + shape1.area )


val shape2 = new Rectangle(10,20)

println("Rectangle Area = " + shape2.area )
