from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    sum,
    avg,
    col
)

spark = SparkSession.builder.getOrCreate()

# Silver Tables
quality = spark.table(
    "workspace.default.production_quality_silver"
)

downtime = spark.table(
    "workspace.default.production_downtime_silver"
)

# Quality Metrics
quality_metrics = (
    quality.groupBy(
        "line_id",
        "equipment_id"
    )
    .agg(
        sum("total_count").alias("total_count"),
        sum("good_count").alias("good_count"),
        sum("defect_count").alias("defect_count"),
        avg("quality_rate").alias("quality_rate")
    )
)

# Downtime Metrics
downtime_metrics = (
    downtime.groupBy(
        "line_id",
        "equipment_id"
    )
    .agg(
        sum("duration_minutes").alias(
            "downtime_minutes"
        )
    )
)

# Join Together
gold = (
    quality_metrics.join(
        downtime_metrics,
        ["line_id", "equipment_id"],
        "left"
    )
)

# Fill null downtime values
gold = gold.fillna(
    {"downtime_minutes": 0}
)

# Save Gold Table
gold.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(
        "workspace.default.oee_metrics_gold"
    )

print("Gold table created")