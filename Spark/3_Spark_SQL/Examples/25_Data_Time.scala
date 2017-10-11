val data = List(
	("2015-08-25 23:59:59", "2015-01-02 00:01:02", 1), //y,M,d,h,m
	("2016-05-12 23:00:00", "2016-01-02 23:59:59", 2),
	("2017-03-27 22:59:58", "2017-01-02 23:59:59", 3)
)


val df = data.toDF().select(
	col("_1").cast("timestamp").alias("start_time"),
	col("_2").cast("timestamp").alias("end_time"),
	col("_3").alias("id")
  )

df.show()

df.select(col("id"), to_date(col("start_time")), hour(col("start_time")),  dayofmonth(col("start_time")), month(col("start_time")), year(col("start_time")) ).show()

df.select(col("id"), expr("start_time + interval 1 day - interval 1 hour") ).show()

df.filter( year(col("start_time"))==="2016" ).show()


val days = List.range(1,10).map(i => "2015-01-" + i.toString  )





