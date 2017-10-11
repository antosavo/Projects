name := "MyProject"

version := "1.0.0"

scalaVersion := "2.11.8"

libraryDependencies += "org.apache.spark" %% "spark-core" % "2.0.1" % "provided"

libraryDependencies += "org.apache.spark" %% "spark-mllib" % "2.0.1" % "provided"

unmanagedJars in Compile += file("breeze-viz-J.jar")