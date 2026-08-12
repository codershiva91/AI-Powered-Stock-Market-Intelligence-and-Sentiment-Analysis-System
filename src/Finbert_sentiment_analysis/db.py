"""
==========================================================
Database Connection Module

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System
==========================================================
"""

import pymysql
from pymysql.cursors import DictCursor

from config import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
)


def get_connection():
    """
    Returns a PyMySQL database connection.
    """

    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",
        cursorclass=DictCursor,
        autocommit=False,
        connect_timeout=10,
    )