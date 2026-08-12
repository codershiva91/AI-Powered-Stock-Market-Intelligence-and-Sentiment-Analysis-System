import pandas as pd
import mariadb
import glob
import os
from dotenv import load_dotenv

load_dotenv()


# ==========================
# Database Connection
# ==========================

# conn = mariadb.connect(
#     host="localhost",
#     user="root",
#     password="@MariaDB123",   # Change if needed
#     database="stock_market_analytics",
#     autocommit=False
# )



conn = mariadb.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="stock_market_analytics",
    autocommit=False
)


cursor = conn.cursor()

# ==========================
# Get All Stock Files
# ==========================

files = glob.glob("data/raw/stocks/*.csv")

print(f"\nFound {len(files)} files\n")

total_rows = 0

# ==========================
# Process Each CSV
# ==========================

for file in files:

    symbol = os.path.basename(file).replace(".csv", "")

    try:

        print(f"Loading {symbol}...")

        df = pd.read_csv(file)

        # Remove extra ticker row
        df = df[df["Date"].notna()]

        # Convert Date
        df["Date"] = pd.to_datetime(df["Date"])

        rows_loaded = 0

        for _, row in df.iterrows():

            cursor.execute(
                """
                INSERT IGNORE INTO stock_prices
                (
                    trade_date,
                    symbol,
                    open_price,
                    high_price,
                    low_price,
                    close_price,
                    adj_close,
                    volume
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    row["Date"].date(),
                    symbol,
                    float(row["Open"]),
                    float(row["High"]),
                    float(row["Low"]),
                    float(row["Close"]),
                    float(row["Adj Close"]),
                    int(row["Volume"])
                )
            )

            rows_loaded += 1

        conn.commit()

        total_rows += rows_loaded

        print(f"✓ Loaded {rows_loaded} rows")

    except Exception as e:

        conn.rollback()

        print(f"✗ Failed {symbol}")
        print(e)

print("\n================================")
print(f"TOTAL ROWS LOADED : {total_rows}")
print("================================")

# ==========================
# Verification
# ==========================

cursor.execute(
    "SELECT COUNT(*) FROM stock_prices"
)

db_count = cursor.fetchone()[0]

print(f"\nRows in Database : {db_count}")

cursor.close()
conn.close()





# import pandas as pd
# import mariadb
# import glob
# import os

# # Connect to MariaDB
# conn = mariadb.connect(
#     host="localhost",
#     user="root",
#     password="@MariaDB123",
#     database="stock_market_analytics",
#     autocommit=True
# )

# cursor = conn.cursor()

# files = glob.glob("data/raw/stocks/*.csv")

# print(f"\nFound {len(files)} files\n")

# total_rows = 0

# for file in files:

#     symbol = os.path.basename(file).replace(".csv", "")

#     try:

#         print(f"Loading {symbol}...")

#         df = pd.read_csv(file)

#         # Remove bad first row
#         df = df[df["Date"].notna()]

#         # Convert date
#         df["Date"] = pd.to_datetime(df["Date"])

#         for _, row in df.iterrows():

#             cursor.execute(
#                 """
#                 INSERT INTO stock_prices
# (
#     trade_date,
#     symbol,
#     open_price,
#     high_price,
#     low_price,
#     close_price,
#     adj_close,
#     volume
# )
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#                 """,
#                 (
#                     row["Date"].date(),
#                     symbol,
#                     float(row["Open"]),
#                     float(row["High"]),
#                     float(row["Low"]),
#                     float(row["Close"]),
#                     float(row["Adj Close"]),
#                     int(row["Volume"])
#                 )
#             )

        

#         total_rows += len(df)

#         print(f"✓ Loaded {len(df)} rows")

#     except Exception as e:

#         print(f"✗ Failed {symbol}")
#         print(e)

# print("\n========================")
# print(f"TOTAL ROWS: {total_rows}")
# print("========================")

# cursor.close()
# conn.close()




# import pandas as pd
# import glob
# import os
# from sqlalchemy import create_engine
# from urllib.parse import quote_plus
# import os

# print("Current Directory:")
# print(os.getcwd())

# # Database Configuration
# DB_USER = "root"
# DB_PASSWORD = quote_plus("@MariaDB1123")
# DB_HOST = "localhost"
# DB_NAME = "stock_market_analytics"

# engine = create_engine(
#     f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
# )

# files = glob.glob("data/raw/stocks/*.csv")

# print(f"Found {len(files)} files")

# total_rows = 0

# for file in files:

#     symbol = os.path.basename(file).replace(".csv", "")

#     try:

#         print(f"\nLoading {symbol}...")

#         df = pd.read_csv(file)

#         # Remove the bad first row
#         df = df[df["Date"].notna()]

#         # Rename columns
#         df.rename(
#             columns={
#                 "Date": "trade_date",
#                 "Open": "open_price",
#                 "High": "high_price",
#                 "Low": "low_price",
#                 "Close": "close_price",
#                 "Adj Close": "adj_close",
#                 "Volume": "volume"
#             },
#             inplace=True
#         )

#         # Add Symbol
#         df["symbol"] = symbol

#         # Convert Date
#         df["trade_date"] = pd.to_datetime(df["trade_date"]).dt.date

#         # Keep required columns
#         df = df[
#             [
#                 "trade_date",
#                 "symbol",
#                 "open_price",
#                 "high_price",
#                 "low_price",
#                 "close_price",
#                 "adj_close",
#                 "volume"
#             ]
#         ]

#         # Load into MariaDB
#         df.to_sql(
#             "stock_prices",
#             con=engine,
#             if_exists="append",
#             index=False,
#             chunksize=1000,
#             method="multi"
#         )

#         total_rows += len(df)

#         print(f"✓ Loaded {len(df)} rows")

#     except Exception as e:

#         print(f"✗ Failed {symbol}")
#         print(e)

# print("\n==============================")
# print(f"TOTAL ROWS LOADED = {total_rows}")
# print("==============================")












# #FINAL PRODUCTION CODE 

# import pandas as pd
# import glob
# import os
# from sqlalchemy import create_engine
# from urllib.parse import quote_plus

# # Database Configuration
# DB_USER = "root"
# DB_PASSWORD = quote_plus("@MariaDB123")
# DB_HOST = "localhost"
# DB_NAME = "stock_market_analytics"

# # Create Engine
# engine = create_engine(
#     f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
# )

# # Get all CSV files
# files = glob.glob("data/raw/stocks/*.csv")

# print(f"\nFound {len(files)} files\n")

# total_rows = 0

# for file in files:

#     symbol = os.path.basename(file).replace(".csv", "")

#     try:

#         print(f"Loading {symbol}...")

#         # Read CSV
#         df = pd.read_csv(file)

#         # Rename Columns
#         df.rename(
#             columns={
#                 "Date": "trade_date",
#                 "Adj Close": "'Adj Close",
#                 "Close": "close_price",
#                 "High": "high_price",
#                 "Low": "low_price",
#                 "Open": "open_price",
#                 "Volume": "volume"
#             },
#             inplace=True
#         )

#         # Add Symbol
#         df["symbol"] = symbol

#         # Keep Required Columns
#         df = df[
#             [
#                 "trade_date",
#                 "symbol",
#                 "open_price",
#                 "high_price",
#                 "low_price",
#                 "close_price",
#                 "adj_close",
#                 "volume"
#             ]
#         ]

#         # Convert Date
#         df["trade_date"] = pd.to_datetime(
#             df["trade_date"]
#         ).dt.date

#         # Remove Null Rows
#         df.dropna(inplace=True)

#         # Load into MariaDB
#         df.to_sql(
#             "stock_prices",
#             con=engine,
#             if_exists="append",
#             index=False,
#             chunksize=1000
#         )

#         total_rows += len(df)

#         print(f"✓ Loaded {len(df)} rows")

#     except Exception as e:

#         print(f"✗ Failed {symbol}")
#         print(e)

# print("\n================================")
# print(f"TOTAL ROWS LOADED: {total_rows}")
# print("================================")



# import pandas as pd
# import glob
# import os
# from sqlalchemy import create_engine

# DB_USER = "root"
# DB_PASSWORD = "@MariaDB123"
# DB_HOST = "localhost"
# DB_NAME = "stock_market_analytics"

# engine = create_engine(
#     f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
# )

# files = glob.glob("data/raw/stocks/*.csv")

# print(f"Found {len(files)} files")

# for file in files:

#     symbol = os.path.basename(file).replace(".csv", "")

#     try:

#         df = pd.read_csv(file)

#         df.columns = [c.lower().strip() for c in df.columns]

#         df["symbol"] = symbol

#         df.rename(
#             columns={
#                 "date": "trade_date",
#                 "open": "open_price",
#                 "high": "high_price",
#                 "low": "low_price",
#                 "close": "close_price",
#                 "adj close": "adj_close"
#             },
#             inplace=True
#         )

#         required_cols = [
#             "trade_date",
#             "symbol",
#             "open_price",
#             "high_price",
#             "low_price",
#             "close_price",
#             "adj_close",
#             "volume"
#         ]

#         df = df[required_cols]

#         df.to_sql(
#             "stock_prices",
#             con=engine,
#             if_exists="append",
#             index=False
#         )

#         print(f"Loaded {symbol}")

#     except Exception as e:

#         print(f"Failed {symbol}: {e}")

# print("Completed")


# import pandas as pd
# import glob
# import os
# from sqlalchemy import create_engine
# from urllib.parse import quote_plus

# # Database Connection
# DB_USER = "root"
# DB_PASSWORD = "@MariaDB123"
# DB_HOST = "localhost"
# DB_NAME = "stock_market_analytics"

# engine = create_engine(
#     f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
# )

# # Get all CSV files
# files = glob.glob("data/raw/stocks/*.csv")

# print(f"\nFound {len(files)} files\n")

# total_rows = 0

# for file in files:

#     symbol = os.path.basename(file).replace(".csv", "")

#     try:

#         print(f"Loading {symbol}")

#         df = pd.read_csv(file)

#         # Rename columns
#         df.rename(
#             columns={
#                 "Date": "trade_date",
#                 "Adj Close": "'Adj Close",
#                 "Close": "close_price",
#                 "High": "high_price",
#                 "Low": "low_price",
#                 "Open": "open_price",
#                 "Volume": "volume"
#             },
#             inplace=True
#         )

#         df["symbol"] = symbol

#         # Select required columns
#         df = df[
#             [
#                 "trade_date",
#                 "symbol",
#                 "open_price",
#                 "high_price",
#                 "low_price",
#                 "close_price",
#                 "adj_close",
#                 "volume"
#             ]
#         ]

#         # Load into MariaDB
#         df.to_sql(
#             name="stock_prices",
#             con=engine,
#             if_exists="append",
#             index=False,
#             chunksize=1000
#         )

#         total_rows += len(df)

#         print(f"✓ Loaded {len(df)} rows")

#     except Exception as e:

#         print(f"✗ Failed {symbol}: {e}")

# print("\n=================================")
# print(f"TOTAL ROWS LOADED: {total_rows}")
# print("=================================")



