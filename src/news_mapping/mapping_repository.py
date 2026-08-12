"""
==============================================================================
News Mapping Repository
==============================================================================

Project : AI-Driven Stock Market Intelligence System

Description
-----------
Repository responsible for all database operations related to
news-to-stock mapping.

Responsibilities
----------------
1. Load companies from symbol_master
2. Load news articles
3. Insert news-stock mappings
4. Load unmapped news articles
5. Bulk insert mappings

==============================================================================
"""

from database.connection import DatabaseConnection
from ai.common.logger import get_logger

logger = get_logger(__name__)


class MappingRepository:

    def __init__(self):

        self.db = DatabaseConnection()

    # ------------------------------------------------------------------

    def load_companies(self):

        """
        Load all companies from symbol_master.
        """

        query = """
        SELECT
            symbol,
            company_name
        FROM symbol_master
        ORDER BY symbol
        """

        return self.db.fetch_all(query)

    # ------------------------------------------------------------------

    def load_news_articles(self):

        """
        Load all news articles.
        """

        query = """
        SELECT
            news_id,
            title,
            article_text
        FROM news_articles
        ORDER BY news_id
        """

        return self.db.fetch_all(query)

    # ------------------------------------------------------------------

    def load_unmapped_news(self):

        """
        Load only news articles that are not yet mapped.
        """

        query = """
        SELECT
            na.news_id,
            na.title,
            na.article_text
        FROM news_articles na

        LEFT JOIN news_stock_mapping sm
            ON na.news_id = sm.news_id

        WHERE sm.news_id IS NULL

        ORDER BY na.news_id
        """

        return self.db.fetch_all(query)

    # ------------------------------------------------------------------

    def insert_mapping(self, news_id, symbol):

        """
        Insert a single mapping.
        """

        query = """
        INSERT IGNORE INTO news_stock_mapping
        (
            news_id,
            symbol,
            relevance_score
        )
        VALUES
        (
            %s,
            %s,
            1.00
        )
        """

        return self.db.execute(query, (news_id, symbol))

    # ------------------------------------------------------------------

    def insert_many(self, values):

        """
        Bulk insert mappings.
        """

        if not values:
            return 0

        query = """
        INSERT IGNORE INTO news_stock_mapping
        (
            news_id,
            symbol,
            relevance_score
        )
        VALUES
        (
            %s,
            %s,
            %s
        )
        """

        return self.db.execute_many(query, values)