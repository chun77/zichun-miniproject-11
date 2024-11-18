# Databricks Data Pipeline

## Description
This project demonstrates a PySpark-based data pipeline using Titanic data. The pipeline processes the data by cleaning and normalizing it, and stores the results in Parquet format.

## Data Source
- The data source is the `titanic.csv` file, uploaded to the Databricks file system (DBFS) at `dbfs:/FileStore/tables/titanic.csv`.

## Data Sink
- The processed data is stored in Parquet format at `dbfs:/output/titanic_processed/`.

## Features
- Reads data from the Titanic dataset uploaded to DBFS.
- Cleans and transforms the data.
- Stores the processed data into a specified sink directory in Parquet format.

## How to Run
1. **Data Source Setup**:
   Upload `titanic.csv` to Databricks at `dbfs:/FileStore/tables/titanic.csv`.

2. **Run the Pipeline**:
   - The pipeline script `src/main.py` reads the source, processes it, and writes the output to the sink.

3. **Check Output**:
   - The output Parquet files are saved in the directory `dbfs:/output/titanic_processed/`.

## CI/CD
- The GitHub Actions workflow automates the execution of the Databricks notebook.
- Ensure your Databricks environment is configured with a valid host and token.

## Output
- The final processed data is saved in Parquet format and can be used for downstream analytics.

