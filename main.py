## run like so:

# spark-submit --master local[10] amazonreviews.py
from pyspark.sql import SparkSession
import statistics

from pyspark.sql.functions import stddev_pop 
from pyspark.sql.types import Row
import numpy as np

def quiet_logs( sc ):
  logger = sc._jvm.org.apache.log4j
  logger.LogManager.getLogger("org"). setLevel( logger.Level.ERROR )
  logger.LogManager.getLogger("akka").setLevel( logger.Level.ERROR )

def f(x):
    d = {}
    for i in range(len(x)):
        d[str(i)] = x[i]
    return d

spark = SparkSession.builder.appName("star stuff").getOrCreate()
## already done, and commented out:

frames = spark.sparkContext.textFile("file:///home/hpistor/cinf401-assignments/cinf401-project-3/stars.txt")
frames = frames.repartition(20)


def stdoutToTuple(x):
    tStr = x[1:-1]
    s = tStr.split(", ")
    y = (float(s[0]), float(s[1]), float(s[2]))
    return y

stars = frames.pipe('/home/hpistor/cinf401-assignments/cinf401-project-3/runopencv.sh').map(lambda x: stdoutToTuple(x))

starsSorted = stars.sortBy(lambda a: a[2], ascending=False)

starsSorted.coalesce(1).saveAsTextFile("file:///home/hpistor/cinf401-assignments/cinf401-project-3/output")
