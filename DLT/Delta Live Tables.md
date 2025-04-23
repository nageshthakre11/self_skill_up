Delta Live Tables:-
    - Declarative by Nature
        - Building Reliable, Maintainable & Testable data processing  pipelines.
        - Developer only need to focus on transformation
        - DLT manages orchestration, cluster management, monitoring, data quality and error handling

    - Allows both Batch and Streaming ingestion

    - Allowed in premium plan of databricks


DLT Pipelines:-
    - Made up of 3 types of datasets
        1. Streaming Tables
        2. Materialized Views
        3. Views

    - Supports Python & SQL Languages

    - Can NOT use ALL SHARED CLUSTER, It requires special type of job compute cluster.


```python
# create streaming table as orders
@dlt.table(
    table_properties = {'quality' = 'bronze'},
    comment = 'order bronze table'
)

def order_bronze():
    df = spark.readStream.table('dev.bronze.order_raw')
    return df


# create materialized view as customers
@dlt.table(
    table_properties = {'quality':'bronze'},
    comment = 'customer bronze table',
    name = 'customer_bronze'
)

def cust_bronze():
    df = spark.read.table('dev.bronze.customer_raw')
    return df


@dlt.view(
    comment = 'view is being created by joining 2 live tables, it is intermedicate view which is notgoing to be stored on any location'
)
def order_customer_join_vw():
    df_order = spark.read.table('LIVE.order_bronze')
    df_customer = spark.read.table('LIVE.cust_bronze')
    joined_vw = df_order.join(df_customer, df_order.o_custmoer_key == df_customer.c_customer_key, 'left_outer')
    return joined_vw
```

while creating the 
    - streaming table, read method is `spark.readStream.table('table_name')` 
    and decorator is `dlt.table()`
    - materialized View, read method is `spark.read.table('table_name')` 
    and decorator is `dlt.table()`
    - view, read method is `spark.read.table('table_name')` and decorator is `dlt.view()`


mode :- 
    - development 
        - cluster keeps on running after pipeline complete run / failure
    - production
        - cluster get kills immediatelly after pipeline complete run / failure

even logs
    - we can see the reason of failure in event 
    
DLT Pipeline:-
    - If I delete DLT pipeline, all datasets will be get deleted.

    - Streaming table is used to process, incremental data 

    - If pipeline is running in development mode, we can very easily connect to the notebook through DLT pipeline, make changes and validate. 


Internal of Delta Live Tables:-
    - When we run DLT pipeline, A hidden catalog `__databricks_internal` has been created and over there delta table will created. 

    - table has pipeline ID, through that ID we can see the delta table location of materialized view / streamining table. 

    - table_id gives the exact location of data stored. 

    - for Streaming Table :- If we look for table_id for streaming table, at the same location we can see `_dlt_metadat` where checkpoint is present, based on checkpoint only , streaming table process incremental data 



DLT Autoloader :-
```python
# create an atoloader 
@dlt.table(
    table_properties = {'quality' : 'bronze'},
    comment = 'created autoloader table',
    name = 'order_autoloader_bronze'
)

def table():
    df = spark.readStream.format('cloudFiles')\
        .option('cloudFiles.schemaLocation', 'path_of_location')
        .option('cloudFiles.format','csv')
        .option('pathGlobFilter','*.csv')
        .option('cloudFiles.schemaEvolutionMode', 'none')
        .load('path_of_files')
    return df
```

*Common decorators used DLT pipeline*
```python
@dlt.table()
@dlt.view()
@dlt.append_flow()
@dlt.except()
@dlt.expect_all()
@dlt.expect_all_or_fail()
@dlt.expect_all_or_drop()
```


```python
@dlt.expect_all("age_check", "age > 18")
@dlt.table
def cleaned_data():
    df = spark.readStream.option("cloudFiles.format", "csv").load("/mnt/data/")
    return 

```

Add parameter to DLT Pipeline
