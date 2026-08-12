"""
==============================================================================
Query Analyzer Entity Extractor
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
Description : Extract companies, indices, sectors, sentiment and time filters.
==============================================================================
"""

import re
from typing import Dict, List

from .database import DatabaseManager
from .config import (
    SUPPORTED_INDICES,
    SUPPORTED_SECTORS,
    TIME_PATTERNS
)
from .logger import get_logger
from .exceptions import EntityExtractionError

logger = get_logger(__name__)


class EntityExtractor:

    def __init__(self):

        self.db = DatabaseManager()

        self.db.load_companies()

        self.company_cache = self.db.get_company_cache()
        self.symbol_lookup = self.db.get_symbol_lookup()
        self.company_lookup = self.db.get_company_lookup()

        logger.info("Entity Extractor initialized.")

    # ======================================================================
    # PUBLIC
    # ======================================================================

    def extract(self, query: str) -> Dict:

        try:

            query = query.upper()

            return {
                "companies": self.extract_companies(query),
                "market_index": self.extract_market_index(query),
                "sector": self.extract_sector(query),
                "sentiment": self.extract_sentiment(query),
                "time_filter": self.extract_time(query)
            }

        except Exception as e:

            logger.exception("Entity Extraction Failed.")

            raise EntityExtractionError(str(e))

    # ======================================================================
    # COMPANY EXTRACTION
    # ======================================================================

    def extract_companies(self, query: str) -> List[Dict]:

        companies = []
        visited = set()

        # Match ticker symbols (TCS, INFY, TCS.NS etc.)
        for symbol, row in self.symbol_lookup.items():

            pattern = rf"\b{re.escape(symbol)}\b"

            if re.search(pattern, query):

                if row["symbol"] not in visited:

                    companies.append(row)
                    visited.add(row["symbol"])

        # Match company names / aliases
        for company, row in self.company_lookup.items():

            pattern = rf"\b{re.escape(company)}\b"

            if re.search(pattern, query):

                if row["symbol"] not in visited:

                    companies.append(row)
                    visited.add(row["symbol"])

        return companies

    # ======================================================================
    # MARKET INDEX
    # ======================================================================

    def extract_market_index(self, query: str):

        indices = sorted(
            SUPPORTED_INDICES,
            key=len,
            reverse=True
        )

        for index in indices:

            pattern = rf"\b{re.escape(index.upper())}\b"

            if re.search(pattern, query):

                return index

        return None

    # ======================================================================
    # SECTOR
    # ======================================================================

    def extract_sector(self, query: str):

        sectors = sorted(
            SUPPORTED_SECTORS,
            key=len,
            reverse=True
        )

        for sector in sectors:

            pattern = rf"\b{re.escape(sector.upper())}\b"

            if re.search(pattern, query):

                return sector

        return None

    # ======================================================================
    # SENTIMENT
    # ======================================================================

    def extract_sentiment(self, query: str):

        mapping = {
            "POSITIVE": ["POSITIVE", "BULLISH"],
            "NEGATIVE": ["NEGATIVE", "BEARISH"],
            "NEUTRAL": ["NEUTRAL"]
        }

        for sentiment, words in mapping.items():

            for word in words:

                pattern = rf"\b{word}\b"

                if re.search(pattern, query):

                    return sentiment

        return None

    # ======================================================================
    # TIME FILTER
    # ======================================================================

    def extract_time(self, query: str):

        q = query.lower()

        for label, patterns in TIME_PATTERNS.items():

            for pattern in patterns:

                if pattern.lower() in q:

                    return label

        return None