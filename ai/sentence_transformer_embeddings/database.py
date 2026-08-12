# """
# Database operations for the Sentence Transformer Embedding module.
# """

# import pymysql
# from pymysql.cursors import DictCursor

# from config import DB_CONFIG, NEWS_TABLE, PRIMARY_KEY, TEXT_COLUMN


# def get_connection():
#     """
#     Create and return a MariaDB database connection.

#     Returns
#     -------
#     pymysql.Connection
#         Active MariaDB connection.
#     """

#     return pymysql.connect(
#         host=DB_CONFIG["host"],
#         port=DB_CONFIG["port"],
#         user=DB_CONFIG["user"],
#         password=DB_CONFIG["password"],
#         database=DB_CONFIG["database"],
#         cursorclass=DictCursor,
#         autocommit=False,
#         charset="utf8mb4"
#     )


# def test_connection() -> bool:
#     """
#     Test the MariaDB connection.

#     Returns
#     -------
#     bool
#         True if the connection succeeds, otherwise False.
#     """

#     connection = None

#     try:
#         connection = get_connection()

#         with connection.cursor() as cursor:
#             cursor.execute("SELECT VERSION();")
#             version = cursor.fetchone()

#         print("=" * 60)
#         print("Database Connected Successfully")
#         print(f"MariaDB Version : {version['VERSION()']}")
#         print("=" * 60)

#         return True

#     except Exception as error:

#         print("=" * 60)
#         print("Database Connection Failed")
#         print(error)
#         print("=" * 60)

#         return False

#     finally:

#         if connection:
#             connection.close()


# def fetch_news_batch(offset: int, batch_size: int):
#     """
#     Fetch a batch of news articles.

#     Parameters
#     ----------
#     offset : int
#         Starting position.

#     batch_size : int
#         Number of rows to fetch.

#     Returns
#     -------
#     list
#         List of news records.
#     """

#     connection = get_connection()

#     try:

#         query = f"""
#             SELECT
#                 {PRIMARY_KEY},
#                 title,
#                 {TEXT_COLUMN}
#             FROM {NEWS_TABLE}
#             ORDER BY {PRIMARY_KEY}
#             LIMIT %s OFFSET %s
#         """

#         with connection.cursor() as cursor:

#             cursor.execute(query, (batch_size, offset))

#             rows = cursor.fetchall()

#         return rows

#     except Exception as error:

#         print(f"Error fetching news batch: {error}")
#         return []

#     finally:

#         connection.close()


# def get_total_news_count() -> int:
#     """
#     Return the total number of news articles.

#     Returns
#     -------
#     int
#         Total records in news table.
#     """

#     connection = get_connection()

#     try:

#         query = f"""
#             SELECT COUNT(*) AS total
#             FROM {NEWS_TABLE}
#         """

#         with connection.cursor() as cursor:

#             cursor.execute(query)

#             result = cursor.fetchone()

#         return result["total"]

#     except Exception as error:

#         print(f"Error getting news count: {error}")
#         return 0

#     finally:

#         connection.close()


# def close_connection(connection):
#     """
#     Safely close a database connection.

#     Parameters
#     ----------
#     connection : pymysql.Connection
#     """

#     if connection:
#         connection.close()

"""
=========================================================
Database Operations
Sentence Transformer Embedding Module

Author : Shivam Sahu
Project : AI Stock Market Intelligence System
=========================================================
"""

import pymysql
from pymysql.cursors import DictCursor

from .config import DB_CONFIG
from .logger import get_logger


logger = get_logger(__name__)


#========================================================
# Database Connection
#=========================================================

def get_connection():
    """
    Create and return a MariaDB connection.
    """

    return pymysql.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        charset="utf8mb4",
        cursorclass=DictCursor,
        autocommit=False
    )


# =========================================================
# Test Connection
# =========================================================

def test_connection():
    """
    Test database connectivity.
    """

    connection = None

    try:

        connection = get_connection()

        with connection.cursor() as cursor:

            cursor.execute("SELECT VERSION() AS version")

            version = cursor.fetchone()

        logger.info("=" * 60)
        logger.info("MariaDB Connected Successfully")
        logger.info(f"Database Version : {version['version']}")
        logger.info("=" * 60)

        return True

    except Exception as e:

        logger.exception("Database Connection Failed")
        return False

    finally:

        if connection:
            connection.close()


# =========================================================
# Total News Count
# =========================================================

def get_total_news_count():
    """
    Return total number of news articles.
    """

    connection = get_connection()

    try:

        query = """
        SELECT COUNT(*) AS total
        FROM news_articles;
        """

        with connection.cursor() as cursor:

            cursor.execute(query)

            result = cursor.fetchone()

        return result["total"]

    except Exception:

        logger.exception("Unable to fetch total news count.")
        return 0

    finally:

        connection.close()


# =========================================================
# Fetch News Batch
# =========================================================

def fetch_news_batch(offset, batch_size):
    """
    Fetch news articles along with sentiment.

    Parameters
    ----------
    offset : int

    batch_size : int

    Returns
    -------
    list[dict]
    """

    connection = get_connection()

    try:

        query = """
        SELECT

            n.news_id,
            n.title,
            n.article_text,
            n.source,
            n.topic,
            n.news_type,
            n.published_at,

            s.sentiment,
            s.confidence_score

        FROM news_articles n

        LEFT JOIN news_sentiment s
            ON n.news_id = s.news_id

        ORDER BY n.news_id

        LIMIT %s OFFSET %s;
        """

        with connection.cursor() as cursor:

            cursor.execute(query, (batch_size, offset))

            rows = cursor.fetchall()

        return rows

    except Exception:

        logger.exception("Unable to fetch news batch.")

        return []

    finally:

        connection.close()


# =========================================================
# Fetch Single News
# =========================================================

def get_news_by_id(news_id):
    """
    Fetch a single news article.

    Parameters
    ----------
    news_id : int

    Returns
    -------
    dict | None
    """

    connection = get_connection()

    try:

        query = """
        SELECT

            n.news_id,
            n.title,
            n.article_text,
            n.source,
            n.topic,
            n.news_type,
            n.published_at,

            s.sentiment,
            s.confidence_score

        FROM news_articles n

        LEFT JOIN news_sentiment s
            ON n.news_id = s.news_id

        WHERE n.news_id=%s;
        """

        with connection.cursor() as cursor:

            cursor.execute(query, (news_id,))

            row = cursor.fetchone()

        return row

    except Exception:

        logger.exception(f"Unable to fetch news_id={news_id}")

        return None

    finally:

        connection.close()


# =========================================================
# Close Connection
# =========================================================

def close_connection(connection):
    """
    Close database connection safely.
    """

    try:

        if connection:
            connection.close()

    except Exception:

        logger.exception("Error closing database connection.")