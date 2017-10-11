import org.apache.spark.ml.feature.VectorAssembler

//Read file

val df = spark.read.
    format("csv").
    option("inferschema", "true").
    option("delimiter"," ").
    load("data_1.txt")

df.show()

//Transform features to dense vector

val Columns = df.columns
val Columns12 = df.columns.slice(1, 3)

val assembler = new VectorAssembler().
  setInputCols(Columns12).//setInputCols(Array("_c1", "_c2")).
  setOutputCol("features")

val training_df = assembler.transform(df).select(col("_c0").cast("Double").as("label"), col("features"))

training_df.show()