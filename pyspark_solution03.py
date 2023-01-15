from pyspark.sql import SparkSession
import json
import os

#os.environ["PYSPARK_PYTHON"] = "C:\Python\Python310"
#os.environ["PYSPARK_DRIVER_PYTHON"] = "C:\Python\Python310"
#os.environ["JAVA_HOME"] = "C:\Program Files\Java\jdk-19"
#os.environ["HADOOP_HOME"] = "C:\Program Files\hadoop-3.2.2\bin"

# Initialize a SparkSession
spark = SparkSession.builder.appName("Address Parser").getOrCreate()

# Create a DataFrame from a list of addresses
address_df = spark.createDataFrame([("4, rue de la revolution",),("200 Broadway Av",),("Calle Aduana, 29",),("Calle 39 No 1540",),("Am Bächle 23",),("Auf der Vogelwiese 23 b",)], ["address"])

# Use SQL to extract the house number and street
address_df.createOrReplaceTempView("address_table")
parsed_address_df = spark.sql("SELECT address, regexp_extract(address, '[0-9]+', 0) as house_number, regexp_replace(address, '[0-9]+', '') as street FROM address_table")
parsed_address_df.toJSON().show()