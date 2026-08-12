#FINAL CODE FOR PRODUCTION


import pandas as pd
import yfinance as yf
import os

# Create folder
os.makedirs("data/raw/stocks", exist_ok=True)

# Read Nifty50 CSV
symbols = pd.read_csv(
    "data/raw/nifty50_constituents.csv"
)

for stock in symbols["Yahoo_Symbol"]:

    try:

        print(f"Downloading {stock}...")

        df = yf.download(
            stock,
            start="2021-01-01",
            end="2026-06-12",
            auto_adjust=False,
            progress=False
        )

        if not df.empty:

            # Convert Date index to normal column
            df.reset_index(inplace=True)

            # Save CSV
            df.to_csv(
                f"data/raw/stocks/{stock}.csv",
                index=False
            )

            print(f"Saved {stock} ({len(df)} rows)")

        else:

            print(f"No data found for {stock}")

    except Exception as e:

        print(f"Failed {stock}: {e}")

print("\nDownload Completed Successfully")


# import pandas as pd
# import yfinance as yf
# import os
# import pymysql

# # MariaDB Connection
# conn = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="@MariaDB1123",
#     database="stock_market_analytics"
# )

# # Get symbols from database
# query = "SELECT symbol FROM symbol_master"
# symbols = pd.read_sql(query, conn)

# # Create folder
# os.makedirs("data/raw/stocks", exist_ok=True)

# # Download data
# for stock in symbols["symbol"]:

#     print(f"Downloading {stock}...")

#     df = yf.download(
#         stock,
#         start="2021-01-01",
#         end="2025-06-12")


# import pandas as pd
# import yfinance as yf
# import os

# # Create folder
# os.makedirs("data/raw/stocks", exist_ok=True)

# # Read Nifty50 CSV
# symbols = pd.read_csv(
#     "data/raw/nifty50_constituents.csv"
# )

# for stock in symbols["Yahoo_Symbol"]:

#     try:

#         print(f"Downloading {stock}...")

#         df = yf.download(
#             stock,
#             start="2021-01-01",
#             end="2026-06-12",
#             auto_adjust=False,
#             progress=False
#         )

#         if len(df) > 0:

#             df.to_csv(
#                 f"data/raw/stocks/{stock}.csv"
#             )

#             print(f"Saved {stock}")

#         else:

#             print(f"No data for {stock}")

#     except Exception as e:

#         print(f"Failed {stock}: {e}")

# print("Download Completed")