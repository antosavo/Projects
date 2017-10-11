import Image.Processing._

val image = readImage("O.png")
writeImage(image,"My_image.png")

val h = heightImage(image)
val w = widthImage(image)

val A = covertToMatrix(image)
val B = covertToGrayMatrix(image)
val C = covertToVector(image)
val D = covertToGrayVector(image)
val E = covertToArray(image)

val rimage = resizeImage(image, 100, 100)
writeImage(rimage,"rimage.png")

val cimage = cropImage(image, 100, 100, 600, 450)//x0,y0,x1,y1
writeImage(cimage,"cimage.png")

val acimage = autoCropImage(image)
writeImage(acimage,"acimage.png")
