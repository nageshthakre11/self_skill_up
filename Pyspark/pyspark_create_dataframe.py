from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('testing').master('local[*]').getOrCreate()

# reading from CSV file 

df_csv = spark.read.option('header', True)\
        .option('inferSchema', True)\
        .option('delimeter',',')\
        .option('qoutes','"')\
        .option('escape','\\')\
        .option('multiLine',True)\
        .option('mode','DROPMALFORMATED')\   # PERMISSIVE / DROPMALFORMATED / FAILFAST
        .csv('path_of_file.csv')

# reading JSON file
df_json = spark.read.option('multiLine', True)\
                .option('mode','PERMISSIVE')\
                .json('json_file_path.json')


# reading delta table by version 
df_delta = spark.read.format("delta") \
    .option("versionAsOf", 5) \
    .load("path/to/delta/table")

# by timestamp
df_delta = spark.read.format("delta") \
    .option("timestampAsOf", "2024-04-10 10:00:00") \
    .load("path/to/delta/table")

# merge schema option 
df_merge_schema = spark.read.format('delta')\
                .option('mergeSchema', True)\
                .load('path_of_delta_table')


# write table
df_delta.write.partitionBy('year','month')\
    .format('delta')\
    .mode('overwrite')\
    .option('overwriteSchema', True)\
    .saveAsTable('db.schema.table_name')


# mode options - overwrite / append / ignore / error


