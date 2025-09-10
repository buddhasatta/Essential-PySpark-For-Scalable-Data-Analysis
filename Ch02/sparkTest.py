from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local[*]").appName("premium").getOrCreate()
rdd1=spark.sparkContext.parallelize([1,2,3])
print(rdd1.collect())