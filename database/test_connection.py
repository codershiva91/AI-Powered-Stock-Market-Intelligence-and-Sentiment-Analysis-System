import mariadb

conn = mariadb.connect(
    host="localhost",
    user="root",
    password="@MariaDB123",
    database="stock_market_analytics"
)

print("SUCCESS")

conn.close()