import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="@MariaDB123",
    database="stock_market_analytics",
    port=3306
)


