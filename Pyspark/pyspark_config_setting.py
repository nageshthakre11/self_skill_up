from pyspark.sql import SparkSession



spark =SparkSession.builder.appName('spark_config').master('local[*]').getOrCreate()



spark.config.set('spark.sql.autoBroadcastJointhreshold', -1)