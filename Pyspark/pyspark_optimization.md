**Code Level Optimization**

1. Avoid RDD operation , stick to DataFrames
2. Avoid Select *, `seelct only` required columns
3. Apply `filter() / where()` operation as early as possible if needed
4. Use `withColumn()` insted of selectExpr() function. 
5. Appropriate use of `cache() / persist()`
6. If not needed , remove unwanted cached dataframe --> `df.unpersist()` 
7. `Broadcast` small DataFrame
8. Avoid `collect()` action, use show() or limit() options 
9. use of `explode()` operation only if necessary 
10. Avoid creating `UDFs`, use pyspark functions
11. Avoid unnecessary shuffling use of `coalesce() and repartition()`
12. setting up repartition on specific column `df.repartition(20, "column_name")`
13. writeing data by `partitionBy('column_name')''` over specific column based on data and further transformations 



1. `Executor Configuration` Set the right balance of cores, memory, and number of executors.
2. `Dynamic Allocation` Automatically adjust the number of executor
```python
        -- conf spark.dynamicAllocation.enabled = True
        -- conf spark.shuffle.service.enabled = True
        -- conf spark.dynamicAllocation.minExecutor = 4
        -- conf spark.dynamicAllocation.maxExecutor = 100
```

3. `Enable adaptive Query Execution AQE`
```python
spark.conf.set("spark.sql.adaptive.enabled", 'True')
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "True")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "True")
```

4. `Shuffle Optimization`
```python
spark.conf.set("spark.sql.shuffle.partitions", 250)
```

5. `Autobroadcast join` 
```python
spark.conf.set("spark.sql.autoBraodcastJoinThreshold",10*1024*1024)
```

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("OptimizedSparkApp") \
    .getOrCreate()

# ✅ Cluster-level & execution tuning
spark.conf.set("spark.dynamicAllocation.enabled", "true")
spark.conf.set("spark.shuffle.service.enabled", "true")
spark.conf.set("spark.dynamicAllocation.minExecutors", "4")
spark.conf.set("spark.dynamicAllocation.maxExecutors", "50")

# ✅ Adaptive Query Execution (AQE)
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

# ✅ Join & Shuffle optimization
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "52428800")  # 50MB
spark.conf.set("spark.sql.shuffle.partitions", "200")

