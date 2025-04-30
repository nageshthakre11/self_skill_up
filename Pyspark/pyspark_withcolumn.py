from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName('transformations').master('local[*]').getOrCreate()

df = spark.read.option('header', True).option('inferSchema', True)\
    .mode('DROPMALFORMATED').csv('path_of_csv_file')


df.withColumn('salary', col('salary').cast(IntegerType()))
df.withColumn('salary', col('salary')* 100)
df.withColumn("Country", lit("INDIA")).show()
df.withColumn('new_slaary', col('salary')+col('salary')*0.80)
df.drop('salary')