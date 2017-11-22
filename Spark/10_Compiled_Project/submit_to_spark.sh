#!/bin/bash
#curr_dir=`pwd`
spark-submit --class PCAHR --master local[1] target/scala-2.11/myproject_2.11-1.0.0.jar
#--class CLASS_NAME specifies the class that contains the main method for your Spark application.
#--master locla[1] means 1 partition. The master URL tells the spark-submit script where you want to run your Spark application.
#--jars JARS to specify a comma-separated list of local jar files to include.
#You can get the complete list of options for the spark-submit script using the --help option "spark-submit --help"
