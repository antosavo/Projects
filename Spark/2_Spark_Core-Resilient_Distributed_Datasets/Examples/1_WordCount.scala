val inputfile = sc.textFile("input.txt")//RDD

val counts = inputfile.
  flatMap(line => line.split(" ")). //to split each line into a Seq of words
  map(word =>(word, 1)).            //to read each word as a key with a value '1' 
  reduceByKey(_+_);                 //to reduce the keys by adding values of similar keys 

counts.saveAsTextFile("output")
//counts.toDebugString  //to know about current RDD 
//counts.cache() //to store the intermediate transformations in memory
//http://localhost:4040 //to see the storage space that is used for this
//application, then use the following URL in your browser.
//counts.unpersist()






