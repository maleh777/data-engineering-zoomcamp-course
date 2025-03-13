import sys
import pandas as pd
import pyarrow.parquet as pq  # For Parquet files
from sqlalchemy import create_engine

try:
    day = sys.argv[1]  # Get the date from command-line arguments

    # 1. Load Parquet Data
    parquet_file = f'yellow_tripdata_{day}.parquet' # Example: yellow_tripdata_2021-01.parquet
    try:
        df = pq.read_table(parquet_file).to_pandas()
        print(f"Parquet file {parquet_file} loaded successfully.")
    except FileNotFoundError:
        print(f"Error: Parquet file {parquet_file} not found. Exiting.")
        sys.exit(1) # Exit with error code

    # 2. Data Transformation (Optional)
    # Add your data transformation logic here if needed.
    # Example:
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # 3. Connect to PostgreSQL
    engine = create_engine('postgresql://root:bmaleh@localhost:5432/ny_taxi')

    # 4. Load Data to PostgreSQL
    table_name = 'yellow_tripdata_trip'  # Your table name
    try:
        df.to_sql(name=table_name, con=engine, index=False, if_exists='append')  # Append data
        print(f"Data loaded to PostgreSQL table {table_name} successfully.")
    except Exception as e:
        print(f"Error loading data to PostgreSQL: {e}")

    print(f'Pipeline finished successfully for day = {day}')

except IndexError:
    print("Error: Date argument is missing. Please provide a date in YYYY-MM format.")
    sys.exit(1)  # Exit with error code
except Exception as e:
    print(f"A general error occurred: {e}")
    sys.exit(1) # Exit with error code
