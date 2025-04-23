from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('autoloader').master('local[*]').getOrCreate()


df = spark.readStream.format('cloudFiles')\
    .option("cloudFiles.format",'csv')\
    .option('pathGlobFilter', "*.csv")\
    .option('header',True)\
    .option('cloudFiles.schemaLocation','Schema_checkpoint_Location_path')\
    .option('schemaEvolutionMode','rescue')\                --> addNewColumns (default) / none /failOnNewColumn
    .load('file_path_location')



df.writeStream\
    .option('checkpointLocation','Schema_checkpoint_Location_path')\
    .outputmode('append')\
    .option('mergeSchema', True)\
    .trigger(availableNow = True)\
    .toTable('db_name.schema_name.table_name')


(spark.readStream.format("cloudFiles")
  .option("cloudFiles.format", "parquet")
  # The schema location directory keeps track of your data schema over time
  .option("cloudFiles.schemaLocation", "<path-to-checkpoint>")
  .load("<path-to-source-data>")
  .writeStream
  .option("checkpointLocation", "<path-to-checkpoint>")
  .start("<path_to_target")
)