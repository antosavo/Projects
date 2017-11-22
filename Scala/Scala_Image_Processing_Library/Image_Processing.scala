package Image

import java.io._
import javax.imageio._
import java.awt._
import java.awt.image.BufferedImage
import java.awt.Graphics2D
import breeze.linalg._

object Processing
{
  
  def readImage(NameFile: String): BufferedImage = 
  {
    val inputfile = new File(NameFile)

    val image = ImageIO.read(inputfile)	

    return image
  }


  def writeImage(image: BufferedImage, NameFile: String)  = 
  {
    val outputfile = new File(NameFile)

    ImageIO.write(image, "png", outputfile)
  }

  def widthImage(image: BufferedImage): Int = 
  {
    val width = image.getWidth

    return width
  }

  def heightImage(image: BufferedImage): Int = 
  {
    val height = image.getHeight

    return height
  }


  def resizeImage(originalImage: BufferedImage, scaledWidth: Int, scaledHeight: Int ): BufferedImage = 
  {
    val scaledBI = new BufferedImage(scaledWidth, scaledHeight, BufferedImage.TYPE_INT_RGB)

    val g = scaledBI.createGraphics()

    g.drawImage(originalImage, 0, 0, scaledWidth, scaledHeight, null)

    g.dispose()

    return scaledBI
  }


  def covertToMatrix(image: BufferedImage): Matrix[Double] = 
  {
    val width = image.getWidth
  
    val height = image.getHeight
  
    var M = Matrix.zeros[Double](height, width)
  
    for(col <- 0 to height - 1)
	{
	    for(row <- 0 to  width - 1) 
	    { 
		M(col,row) = image.getRGB(row,col).toDouble 
	    }
	}
 
    return M
  }


  def covertToGrayMatrix(image: BufferedImage): Matrix[Double] = 
  {
    val width = image.getWidth

    val height = image.getHeight

    var M = Matrix.zeros[Double](height, width)

    for(col <- 0 to height - 1)
	{
	    for(row <- 0 to  width - 1) 
	    { 
		val c = new Color(image.getRGB(row, col))
            
		val red = c.getRed()*0.33
		val green = c.getGreen()*0.33
		val blue = c.getBlue()*0.34
            
		val sum = (red+green+blue).toInt
            
		val newColor = new Color(sum,sum,sum)
            
		image.setRGB(row,col,newColor.getRGB())
            
		M(col,row) = image.getRGB(row,col).toDouble 
	  }
      }
 
    return M
  }

  def covertToArray(image: BufferedImage): Array[Double] = 
  {
    val width = image.getWidth

    val height = image.getHeight

    var V = new Array[Double](height*width)

    var j = 0

    for(col <- 0 to height - 1)
	{
	    for(row <- 0 to  width - 1) 
	    { 
		V(j) = image.getRGB(row,col).toDouble
		j = j + 1
	    }
	}
 
    return V
  }


  def covertToVector(image: BufferedImage): DenseVector[Double] = 
  {
    val width = image.getWidth

    val height = image.getHeight

    var V = DenseVector.zeros[Double](height*width)

    var j = 0

    for(col <- 0 to height - 1)
	{
	    for(row <- 0 to  width - 1) 
	    { 
		V(j) = image.getRGB(row,col).toDouble
		j = j + 1
	    }
	}
 
    return V
  }


  def covertToGrayVector(image: BufferedImage): DenseVector[Double] = 
  {
    val width = image.getWidth

    val height = image.getHeight

    var V = DenseVector.zeros[Double](height*width)

    var j = 0

    for(col <- 0 to height - 1)
	{
	    for(row <- 0 to  width - 1) 
	    { 	      
		val c = new Color(image.getRGB(row, col))
            
		val red = c.getRed()*0.33
		val green = c.getGreen()*0.33
		val blue = c.getBlue()*0.34
            
		val sum = (red+green+blue).toInt
            
		val newColor = new Color(sum,sum,sum)
            
		image.setRGB(row,col,newColor.getRGB())
            
		V(j) = image.getRGB(row,col).toDouble
		
		j = j + 1
	    }
	}
 
    return V
  }


  def cropImage(image: BufferedImage, x0: Int, y0: Int, x1:Int, y1: Int): BufferedImage = 
  {
    val imc = image.getSubimage(x0,y0,x1-x0,y1-y0)//(x0,y0,dx,dy)
    return imc
  }

  def autoCropImage(image: BufferedImage): BufferedImage = 
  {
    val width = image.getWidth
    val height = image.getHeight
    val h0 = image.getRGB(0,0)
    var h = image.getRGB(0,0)
    var col = 0
    var row = 0

  //get y0
    while(col < height && h == h0)
      {
	row = 0
    
	while(row < width && h == h0)
	  {
	    h = image.getRGB(row,col)
	    row = row + 1
	  }
  
	col = col + 1
      }
  
    val y0 = col - 1
  
    //get y1	
    col = height - 1
    h = image.getRGB(0,0)
  
    while(col >=0 && h == h0)
      {
	row = 0
    
	while(row < width && h == h0)
	  {
	    h = image.getRGB(row,col)
	    row = row + 1
	  }
  
	col = col - 1
      }
  
    val y1 = col + 1
    
    //get x0
    row = 0
    h = image.getRGB(0,0)
    
    while(row < width && h == h0)
      {
	col = 0
    
	while(col < height && h == h0)
	  {
	    h = image.getRGB(row,col)
	    col = col + 1
	  }
  
	row = row + 1
      }

    val x0 = row -1
    
    //get x1
    row = width - 1
    h = image.getRGB(0,0)
    
    while(row >=0 && h == h0)
      {
	col = 0
    
	while(col < height && h == h0)
	  {
	    h = image.getRGB(row,col)
	    col = col + 1
	  }
    
	row = row - 1
      }
  
    val x1 = row + 1
  
    val imc = image.getSubimage(x0,y0,x1-x0,y1-y0)//(x0,y0,dx,dy)
    
    return imc
  }


}