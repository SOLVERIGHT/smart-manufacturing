from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

base_path = "/Workspace/Users/seth.ms07g@nctu.edu.tw/.bundle/oee-analytics/dev/files/data/sample"

quality_path = f"{base_path}/quality_logs.csv"
downtime_path = f"{base_path}/downtime_logs.csv"

quality_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(quality_path)
)

downtime_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(downtime_path)
)

quality_df.write.mode("overwrite").saveAsTable("quality_logs_bronze")
downtime_df.write.mode("overwrite").saveAsTable("downtime_logs_bronze")

print("Bronze tables created successfully")