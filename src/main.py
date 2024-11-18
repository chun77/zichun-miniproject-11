from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, stddev

spark = SparkSession.builder.appName("Titanic Data Pipeline").getOrCreate()

source_path = "dbfs:/FileStore/tables/titanic.csv"

sink_path = "dbfs:/output/titanic_processed/"

print(f"Reading data from source: {source_path}")
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(source_path)

columns_to_select = ["Survived", "Pclass", "Sex", "Age", "Fare"]
df_cleaned = df.select(columns_to_select).dropna()
print(f"Data cleaning completed. Remaining rows: {df_cleaned.count()}")

fare_mean = df_cleaned.select(mean(col("Fare"))).collect()[0][0]
fare_stddev = df_cleaned.select(stddev(col("Fare"))).collect()[0][0]
df_transformed = df_cleaned.withColumn("Fare_Normalized", (col("Fare") - fare_mean) / fare_stddev)
print("Data transformation completed.")

print(f"Saving processed data to sink: {sink_path}")
df_transformed.write.format("parquet").mode("overwrite").save(sink_path)
print(f"Data successfully saved to {sink_path}")
