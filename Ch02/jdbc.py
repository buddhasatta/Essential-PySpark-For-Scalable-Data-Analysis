from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local[*]").appName("local2").config("spark.jars","/Users/buddhasattaduttaroy/Documents/PySpark/mariadb-java-client-3.5.5.jar").getOrCreate()
dataframe_mysql =spark.read.format("jdbc").options(
  url="jdbc:mariadb://localhost:3306/geeks_for_geeks",
  driver="org.mariadb.jdbc.Driver",
  dbtable="product",
  header="true",
  user="root",
  password="Alpha.2.0").load()

dataframe_mysql=dataframe_mysql.filter("`product_id` != `product_id`")
dataframe_mysql.createTempView("product")
spark.sql("select * from product").show()