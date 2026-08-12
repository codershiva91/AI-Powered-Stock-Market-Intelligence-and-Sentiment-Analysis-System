"""
==============================================================================
Stock Repository
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Repository responsible for fetching structured stock market data from MariaDB.

Responsibilities
----------------
1. Latest Stock Price
2. Technical Indicators
3. Company Fundamentals
4. Aggregated Company Sentiment
5. Market Index Data

==============================================================================
"""

from typing import Optional, Dict, Any

from database.connection import DatabaseConnection
from ai.common.logger import get_logger

logger = get_logger(__name__)


class StockRepository:
    """
    Repository for stock-related database operations.
    """

    def __init__(self):
        self.db = DatabaseConnection()
        logger.info("StockRepository initialized.")

    # ------------------------------------------------------------------
    # Latest Stock Price
    # ------------------------------------------------------------------

    def get_latest_price(self, symbol: str) -> Optional[Dict[str, Any]]:
        """
        Get latest stock price.
        """

        query = """
        SELECT
            trade_date,
            open_price,
            high_price,
            low_price,
            close_price,
            volume
        FROM stock_prices
        WHERE symbol=%s
        ORDER BY trade_date DESC
        LIMIT 1
        """

        return self.db.fetch_one(query, (symbol,))

    # ------------------------------------------------------------------
    # Technical Indicators
    # ------------------------------------------------------------------

    def get_technical_indicators(
        self,
        symbol: str
    ) -> Optional[Dict[str, Any]]:
        """
        Get latest technical indicators.
        """

        query = """
        SELECT

            trade_date,
            symbol,

            sma_20,
            sma_50,

            ema_20,

            rsi_14,

            macd,
            macd_signal,

            bb_upper,
            bb_lower

        FROM technical_indicators

        WHERE symbol=%s

        ORDER BY trade_date DESC

        LIMIT 1
        """

        return self.db.fetch_one(query, (symbol,))

    # ------------------------------------------------------------------
    # Company Fundamentals
    # ------------------------------------------------------------------

    def get_company_fundamentals(
        self,
        symbol: str
    ) -> Optional[Dict[str, Any]]:
        """
        Get company fundamentals.
        """

        query = """
        SELECT *
        FROM company_fundamentals
        WHERE symbol=%s
        """

        return self.db.fetch_one(query, (symbol,))

    # ------------------------------------------------------------------
    # Company Sentiment
    # ------------------------------------------------------------------

    def get_company_sentiment(
        self,
        symbol: str
    ) -> Optional[Dict[str, Any]]:
        """
        Get aggregated FinBERT sentiment for a company.
        """

        query = """
        SELECT

            CASE
                WHEN SUM(CASE WHEN ns.sentiment='Positive' THEN 1 ELSE 0 END)
                   > SUM(CASE WHEN ns.sentiment='Negative' THEN 1 ELSE 0 END)
                    THEN 'Positive'

                WHEN SUM(CASE WHEN ns.sentiment='Negative' THEN 1 ELSE 0 END)
                   > SUM(CASE WHEN ns.sentiment='Positive' THEN 1 ELSE 0 END)
                    THEN 'Negative'

                ELSE 'Neutral'
            END AS overall_sentiment,

            ROUND(AVG(ns.confidence_score),4) AS confidence,

            SUM(CASE WHEN ns.sentiment='Positive' THEN 1 ELSE 0 END)
                AS positive_count,

            SUM(CASE WHEN ns.sentiment='Neutral' THEN 1 ELSE 0 END)
                AS neutral_count,

            SUM(CASE WHEN ns.sentiment='Negative' THEN 1 ELSE 0 END)
                AS negative_count

        FROM news_sentiment ns

        INNER JOIN news_stock_mapping nsm
            ON ns.news_id = nsm.news_id

        WHERE nsm.symbol = %s
        """

        sentiment = self.db.fetch_one(query, (symbol,))

        if sentiment and sentiment["confidence"] is not None:

            logger.info(
                "Sentiment retrieved for %s : %s",
                symbol,
                sentiment["overall_sentiment"]
            )

            return sentiment

        logger.warning(
            "No sentiment found for %s",
            symbol
        )

        return {
            "overall_sentiment": "Neutral",
            "confidence": 0.0,
            "positive_count": 0,
            "neutral_count": 0,
            "negative_count": 0,
        }

    #------------------------------------------------------------------
       # Market Index
    #------------------------------------------------------------------

    def get_market_index(
        self,
        index_name: str
    ) -> Optional[Dict[str, Any]]:
        """
        Get latest market index.
        """

        query = """
        SELECT *
        FROM market_indices
        WHERE index_name=%s
        ORDER BY trade_date DESC
        LIMIT 1
        """

        return self.db.fetch_one(query, (index_name,))

        # ------------------------------------------------------------------
    # Dashboard Statistics
    # ------------------------------------------------------------------

    def get_company_count(self) -> int:
        """
        Get total number of listed companies.
        """
        query = """
        SELECT COUNT(*) AS total
        FROM symbol_master
        """

        result = self.db.fetch_one(query)
        return result["total"] if result else 0

    # ------------------------------------------------------------------

    def get_news_count(self) -> int:
        """
        Get total number of news articles.
        """
        query = """
        SELECT COUNT(*) AS total
        FROM news_articles
        """

        result = self.db.fetch_one(query)
        return result["total"] if result else 0

    # ------------------------------------------------------------------

    def get_sentiment_count(self) -> int:
        """
        Get total number of sentiment records.
        """
        query = """
        SELECT COUNT(*) AS total
        FROM news_sentiment
        """

        result = self.db.fetch_one(query)
        return result["total"] if result else 0

    # ------------------------------------------------------------------

    def get_stock_price_count(self) -> int:
        """
        Get total number of stock price records.
        """
        query = """
        SELECT COUNT(*) AS total
        FROM stock_prices
        """

        result = self.db.fetch_one(query)
        return result["total"] if result else 0

    #------------------------------------------------------------------

    def get_technical_indicator_count(self) -> int:
        """
        Get total number of technical indicator records.
        """
        query = """
        SELECT COUNT(*) AS total
        FROM technical_indicators
        """

        result = self.db.fetch_one(query)
        return result["total"] if result else 0
    
    #------------------------------------------------------------------
    # Company List
    # ------------------------------------------------------------------

    def get_all_companies(self):
        """
        Get all listed companies for dashboard dropdown.
        """

        query = """
        SELECT
            symbol,
            company_name
        FROM symbol_master
        ORDER BY company_name
        """

        return self.db.fetch_all(query)
    
    #=======================
    #1. Latest NIFTY Index
    #=======================
    
    def get_latest_market_index(self, index_name:str="NIFTY50"):

        query = """
    SELECT *
    FROM market_indices
    WHERE index_name=%s
    ORDER BY trade_date DESC
    LIMIT 1
    """

        return self.db.fetch_one(query, (index_name,))
    
    #=========================
    #2. Top Gainers
    #=========================
    
    def get_top_gainers(self, limit=5):

        query = """
    SELECT

        symbol,

        close_price,

        ROUND(
            ((close_price - open_price) / open_price) * 100,
            2
        ) AS daily_return

    FROM stock_prices

    WHERE trade_date = (
        SELECT MAX(trade_date)
        FROM stock_prices
    )

    ORDER BY daily_return DESC

    LIMIT %s
    """

        return self.db.fetch_all(query, (limit,))
    
    
    
    #========================
    #3. Top Losers
    #=========================
    
    def get_top_losers(self, limit=5):

        query = """
    SELECT

        symbol,

        close_price,

        ROUND(
            ((close_price - open_price) / open_price) * 100,
            2
        ) AS daily_return

    FROM stock_prices

    WHERE trade_date = (
        SELECT MAX(trade_date)
        FROM stock_prices
    )

    ORDER BY daily_return ASC

    LIMIT %s
    """

        return self.db.fetch_all(query, (limit,))
    
    #=========================
    #4. Overall Market Sentiment
    #============================
    
    def get_market_sentiment(self):

        query = """
    SELECT

        SUM(sentiment='Positive') AS positive,

        SUM(sentiment='Neutral') AS neutral,

        SUM(sentiment='Negative') AS negative

    FROM news_sentiment
    """

        return self.db.fetch_one(query)
    
    #=========================
    #5. Market Statistics
    #=========================
    def get_market_statistics(self):

        query = """
    SELECT

        COUNT(DISTINCT symbol) AS total_companies,

        ROUND(AVG(close_price),2) AS average_price,

        MAX(close_price) AS highest_price,

        MIN(close_price) AS lowest_price

    FROM stock_prices

    WHERE trade_date = (
        SELECT MAX(trade_date)
        FROM stock_prices
    )
    """

        return self.db.fetch_one(query)
    
    
    
    # ==========================================
    # 6. Market History (Candlestick Chart)
    # ==========================================

    def get_market_history(
        self,
        index_name="NIFTY50",
        limit=90,
    ):
        """
        Get market index history for dashboard charts.
        """

        query = """
        SELECT
            trade_date,
            open_price,
            high_price,
            low_price,
            close_price,
            volume
        FROM market_indices
        WHERE index_name=%s
        ORDER BY trade_date ASC
        LIMIT %s
        """

        return self.db.fetch_all(
            query,
            (index_name, limit),
            
        )
    # ==========================================================
# 7. Company Price History
# ==========================================================

def get_company_price_history(
    self,
    symbol: str,
    limit: int = 90,
):
    """
    Returns historical OHLCV data for a company.
    """

    query = """
    SELECT

        trade_date,
        open_price,
        high_price,
        low_price,
        close_price,
        volume

    FROM stock_prices

    WHERE symbol=%s

    ORDER BY trade_date DESC

    LIMIT %s
    """

    rows = self.db.fetch_all(
        query,
        (symbol, limit),
    )

    if rows:
        rows.reverse()

    return rows   
        
#----------------------------------------------------------------------
# Testing
# ----------------------------------------------------------------------

if __name__ == "__main__":

    repo = StockRepository()

    print("\nAvailable Methods:\n")

    methods = [
        method
        for method in dir(repo)
        if callable(getattr(repo, method)) and not method.startswith("__")
    ]

    for method in methods:
        print(method)