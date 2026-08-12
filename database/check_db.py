# import mariadb

# conn = mariadb.connect(
#     host="localhost",
#     user="root",
#     password="@MariaDB123",   # use the same password as loader
#     database="stock_market_analytics"
# )

# # cursor = conn.cursor()

# # cursor.execute("SELECT COUNT(*) FROM stock_prices")

# # print("Rows:", cursor.fetchone()[0])

# # cursor.close()
# # conn.close()


import os
import mariadb
from dotenv import load_dotenv

load_dotenv()

conn = mariadb.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="stock_market_analytics"
)

# cursor = conn.cursor()

# cursor.execute("SELECT COUNT(*) FROM stock_prices")

# print("Rows:", cursor.fetchone()[0])

# cursor.close()

# conn.close()