

import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

# Step 1: Extract JSON Data from API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convert API response to JSON
else:
    raise Exception("Failed to fetch data from API")

# Step 2: Initialize Spark Session
spark = SparkSession.builder.appName("Nested_JSON_ETL").getOrCreate()

# Step 3: Load JSON Data into Spark DataFrame
df = spark.createDataFrame(data)

# Step 4: Handle Nested JSON
# Extract fields from the nested "author" object
df_flattened = df.select(
    col("userId"),
    col("id"),
    col("title"),
    col("body"),
    col("author.name").alias("author_name"),
    col("author.email").alias("author_email")
)

# Step 5: Explode Nested Array (comments)
if "comments" in df.columns:
    df_exploded = df.withColumn("comment", explode(col("comments"))) \
                     .select(
                         col("id"),
                         col("comment.comment_id"),
                         col("comment.text"),
                         col("comment.user").alias("comment_user")
                     )
else:
    df_exploded = None