from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName('transformations').master('local[*]').getOrCreate()

df = spark.read.option('header', True).option('inferSchema', True)\
    .mode('DROPMALFORMATED').csv('path_of_csv_file')


# column name  rename
df2 = df.withColumnRenamed("dob","DateOfBirth") \
    .withColumnRenamed("salary","salary_amount")
df2.printSchema()

# PySpark StructType
df.select(col("name").cast(schema2), \
     col("dob"), col("gender"),col("salary")) \
   .printSchema()  

# Select – To rename nested elements.

df.select(col("name.firstname").alias("fname"), \
  col("name.middlename").alias("mname"), \
  col("name.lastname").alias("lname"), \
  col("dob"),\
  col("gender"),\
  col("salary")).printSchema()

# using withColumn()
from pyspark.sql.functions import *
df4 = df.withColumn("fname",col("name.firstname")) \
      .withColumn("mname",col("name.middlename")) \
      .withColumn("lname",col("name.lastname")) \
      .drop("name")
df4.printSchema()
