"""
==============================================================================
Database Connection Manager
==============================================================================

Project : AI-Driven Stock Market Intelligence System

Description
-----------
Reusable PyMySQL connection manager.

Used by:
    - StockRepository
    - NewsRepository
    - Future repositories

==============================================================================
"""

import pymysql

from config.db_config import DB_CONFIG
from ai.common.logger import get_logger


logger = get_logger(__name__)


class DatabaseConnection:

    def __init__(self):

        logger.info("Initializing Database Connection...")

    # ---------------------------------------------------------

    def get_connection(self):

        return pymysql.connect(**DB_CONFIG)

    # ---------------------------------------------------------

    def fetch_one(self, query, params=None):

        conn = None

        try:

            conn = self.get_connection()

            with conn.cursor() as cursor:

                cursor.execute(query, params)

                return cursor.fetchone()

        except Exception as e:

            logger.exception(e)

            return None

        finally:

            if conn:
                conn.close()

    # ---------------------------------------------------------

    def fetch_all(self, query, params=None):

        conn = None

        try:

            conn = self.get_connection()

            with conn.cursor() as cursor:

                cursor.execute(query, params)

                return cursor.fetchall()

        except Exception as e:

            logger.exception(e)

            return []

        finally:

            if conn:
                conn.close()

    # ---------------------------------------------------------

    def execute(self, query, params=None):

        conn = None

        try:

            conn = self.get_connection()

            with conn.cursor() as cursor:

                cursor.execute(query, params)

                conn.commit()

                return cursor.rowcount

        except Exception as e:

            if conn:
                conn.rollback()

            logger.exception(e)

            return 0

        finally:

            if conn:
                conn.close()

    # ---------------------------------------------------------

    def execute_many(self, query, values):

        conn = None

        try:

            conn = self.get_connection()

            with conn.cursor() as cursor:

                cursor.executemany(query, values)

                conn.commit()

                return cursor.rowcount

        except Exception as e:

            if conn:
                conn.rollback()

            logger.exception(e)

            return 0

        finally:

            if conn:
                conn.close()

    # ---------------------------------------------------------

    def test_connection(self):

        conn = None

        try:

            conn = self.get_connection()

            with conn.cursor() as cursor:

                cursor.execute("SELECT 1")

                cursor.fetchone()

            logger.info("Database connected successfully.")

            return True

        except Exception as e:

            logger.exception(e)

            return False

        finally:

            if conn:
                conn.close()