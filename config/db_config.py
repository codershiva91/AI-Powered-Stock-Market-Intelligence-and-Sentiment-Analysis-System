#DB_CONFIG = {
#     "host": "localhost",
#     "user": "root",
#     "password": "@MariaDB123",
#     "database": "stock_market_analytics",
#     "port": 3306
# }


import pymysql

import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": os.getenv("DB_PASSWORD"),
    "database": "stock_market_analytics",
    "port": 3306,
    "cursorclass": pymysql.cursors.DictCursor,
    "charset": "utf8mb4"
}