from pyspark.sql import SparkSession
from pyspark.sql.functions import try_to_timestamp, col, lit

spark = SparkSession.builder.getOrCreate()

quality = (
    spark.table("workspace.default.quality_logs_bronze")
    .withColumn(
        "event_ts",
        try_to_timestamp(col("event_ts"), lit("yyyy/M/d HH:mm"))
    )
    .withColumn("source", lit("quality"))
)

downtime = (
    spark.table("workspace.default.downtime_logs_bronze")
    .withColumn(
        "event_ts",
        try_to_timestamp(col("event_ts"), lit("yyyy/M/d HH:mm"))
    )
    .withColumn("source", lit("downtime"))
)

quality_clean = (
    quality.select(
        "event_ts",
        "line_id",
        "equipment_id",
        "product_id",
        "total_count",
        "good_count",
        "defect_count",
        "inspection_result",
        "source"
    )
    .filter(col("event_ts").isNotNull())
    .filter(col("total_count") > 0)
    .filter(col("good_count") <= col("total_count"))
    .withColumn(
        "quality_rate",
        col("good_count") / col("total_count")
    )
)

downtime_clean = (
    downtime.select(
        "event_ts",
        "line_id",
        "equipment_id",
        "downtime_type",
        "reason",
        "duration_minutes",
        "source"
    )
    .filter(col("event_ts").isNotNull())
    .filter(col("duration_minutes") >= 0)
)

quality_clean.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("workspace.default.production_quality_silver")

downtime_clean.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("workspace.default.production_downtime_silver")

print("Silver tables created successfully")