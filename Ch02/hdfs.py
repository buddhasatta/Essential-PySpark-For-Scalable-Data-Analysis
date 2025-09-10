from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local[*]").appName("local2").config("spark.jars","/Users/buddhasattaduttaroy/Documents/PySpark/mariadb-java-client-3.5.5.jar").getOrCreate()
df=spark.read.csv("hdfs://localhost:9000/files/simple-zipcodes.csv",inferSchema=True,header=True)
df.show(10)


