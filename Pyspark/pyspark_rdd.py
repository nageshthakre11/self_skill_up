# count the number of words present in list / file 
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('testing').master("local[*]").getOrCreate()

sc = spark.SparkContext()
matter = ['we are writing this code to count the words present in the paragraph. We are dealing with RDD using flatmap and map function.']
data = sc.parallelize(matter)   # read text from matter as above mentioned
data = sc.textFile('abc.txt')  # read text file 

data1 = data.flatmap(lambda x: x.split(' '))\
            .map(lambda x: (x,1))\
            .reduceByKey(lambda x,y: x+y)

data1.collect()
                 