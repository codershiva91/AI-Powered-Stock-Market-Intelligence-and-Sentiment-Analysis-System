"""
==============================================================================
Query Analyzer Database Manager
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
Description : Database helper for Query Analyzer V2
==============================================================================

Responsibilities
----------------
1. Connect to MariaDB
2. Load company master data
3. Cache company information
4. Provide lookup methods
==============================================================================

"""

import pymysql
from typing import Dict, List

from config.db_config import DB_CONFIG

from .logger import get_logger
from .exceptions import (
    DatabaseConnectionError,
    CompanyLoadingError
)

logger = get_logger(__name__)


class DatabaseManager:
    """
    Database manager for Query Analyzer.

    Loads company information from symbol_master only once
    and caches it for fast lookups.
    """

    def __init__(self):

        self.connection = None

        self.company_cache = []

        self.symbol_lookup = {}

        self.company_lookup = {}

    # ======================================================================
    # DATABASE CONNECTION
    # ======================================================================

    def connect(self):

        try:

            if self.connection is None:

                logger.info("Connecting to MariaDB...")

                self.connection = pymysql.connect(**DB_CONFIG)

                logger.info("MariaDB connection established.")

            return self.connection

        except Exception as e:

            logger.exception("Database connection failed.")

            raise DatabaseConnectionError(str(e))

    # ======================================================================
    # LOAD COMPANY MASTER
    # ======================================================================

    def load_companies(self):

        """
        Load all companies from symbol_master.
        """

        if self.company_cache:

            logger.info(
                "Using cached company master (%d companies).",
                len(self.company_cache)
            )

            return self.company_cache

        connection = self.connect()

        try:

            with connection.cursor() as cursor:

                sql = """
                    SELECT
                        symbol,
                        company_name
                    FROM symbol_master
                    ORDER BY company_name
                """

                cursor.execute(sql)

                rows = cursor.fetchall()

            if not rows:

                raise CompanyLoadingError(
                    "No companies found in symbol_master."
                )

            self.company_cache = rows

            # =============================================================
            # Build Lookup Dictionaries
            # =============================================================

            aliases = {
                "RELIANCE INDUSTRIES": ["RELIANCE"],
                "TATA CONSULTANCY SERVICES": ["TCS"],
                "INFOSYS": ["INFY"],
                "WIPRO": ["WIPRO"],
                "HDFC BANK": ["HDFC"],
                "ICICI BANK": ["ICICI"],
                "STATE BANK OF INDIA": ["SBI", "SBIN"],
                "TATA MOTORS": ["TATAMOTORS"],
                "LARSEN & TOUBRO": ["L&T", "LT"]
            }

            for row in rows:

                symbol = row["symbol"].upper().strip()
                company = row["company_name"].upper().strip()

                # ----------------------------
                # Store original symbol
                # Example : TCS.NS
                # ----------------------------
                self.symbol_lookup[symbol] = row

                # ----------------------------
                # Store clean symbol
                # Example : TCS
                # ----------------------------
                clean_symbol = symbol.replace(".NS", "")
                self.symbol_lookup[clean_symbol] = row

                # ----------------------------
                # Store company name
                # ----------------------------
                self.company_lookup[company] = row

                # ----------------------------
                # Store aliases
                # ----------------------------
                if company in aliases:

                    for alias in aliases[company]:

                        self.company_lookup[alias.upper()] = row

            logger.info(
                "Loaded %d companies from symbol_master.",
                len(rows)
            )

            logger.info(
                "Company lookup entries : %d",
                len(self.company_lookup)
            )

            logger.info(
                "Symbol lookup entries : %d",
                len(self.symbol_lookup)
            )

            return rows

        except Exception as e:

            logger.exception("Unable to load company master.")

            raise CompanyLoadingError(str(e))

    # ======================================================================
    # GET COMPANY CACHE
    # ======================================================================

    def get_company_cache(self):

        if not self.company_cache:

            self.load_companies()

        return self.company_cache

    # ======================================================================
    # GET SYMBOL LOOKUP
    # ======================================================================

    def get_symbol_lookup(self):

        if not self.symbol_lookup:

            self.load_companies()

        return self.symbol_lookup

    # ======================================================================
    # GET COMPANY LOOKUP
    # ======================================================================

    def get_company_lookup(self):

        if not self.company_lookup:

            self.load_companies()

        return self.company_lookup

    # ======================================================================
    # CLOSE CONNECTION
    # ======================================================================

    def close(self):

        try:

            if self.connection:

                self.connection.close()

                logger.info("Database connection closed.")

                self.connection = None

        except Exception:

            logger.exception("Error while closing database.")