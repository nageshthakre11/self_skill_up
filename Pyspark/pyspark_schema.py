# define the spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('practice').master("local[*]").getOrCreate()


# define the schema using StructType

from pyspark.sql.functions import SructType, StructField, StringType, IntegerType

schema = StructType([
        StrcutField("ID", IntegerType(), True),
        StructField("NAME", StringType(), True)
        ])
        
df = spark.read.csv('file.txt', schema = schema, header = True)

###---------------------------

# Create DataFrame
data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)


#-------------create datafram ----------------------

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Initialize Spark session
spark = SparkSession.builder.appName("CreateDFWithSchema").getOrCreate()

# Step 1: Define data
data = [
    (1, "Alice", 30),
    (2, "Bob", 25),
    (3, "Charlie", 35)
]

# ------------------- Step 2: Define schema ----------------------
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Step 3: Create DataFrame
df = spark.createDataFrame(data, schema)


# -------------------SQL DDL Method ---------------------
schema = "name STRING, age INT, city STRING"
df = spark.read.schema(schema).csv("path/to/file.csv", header=True)


# ---------- create datafrme using python list and tuples -----------------

data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
columns = ["name", "age"]

df = spark.createDataFrame(data, schema=columns)


# --------------create dataframe from RDD ---------------------
rdd = spark.SparkContext([('nagesh',32),('Pallavi',29)])
df = rdd.toDF(['name','age'])

# -- OR

schema_rdd = SructType([StructField('Name', StringType(),True),
                        StructField('Age',IntegerType(), True) ])
df = spark.createDataFrame(rdd, schema_rdd)




# ------------------------To get number of partitions-----------------------------------
from pyspark.sql import spark_partition_id

df.rdd.genNumPartitions()    # to get number of partitions

df.withColumn('partition_id', spark_partition_id()).groupBy('partition_id').count()
# get number of items in partitions using spark

df.rdd.glom().map(len).collec()
# get number of items in partitions from rdd using glom() function