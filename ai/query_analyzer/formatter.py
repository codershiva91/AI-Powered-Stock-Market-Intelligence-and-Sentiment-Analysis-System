"""
==============================================================================
Query Analyzer Formatter
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
Description : Formats the final output of Query Analyzer V2
==============================================================================

"""

from datetime import datetime
from typing import Dict

from .logger import get_logger
from .exceptions import QueryFormattingError

logger = get_logger(__name__)


class QueryFormatter:
    """
    Combines intent and extracted entities into
    a standard output format.
    """

    def __init__(self):

        logger.info("Query Formatter initialized.")

    # ======================================================================
    # FORMAT
    # ======================================================================

    def format(
        self,
        query: str,
        intent_result: Dict,
        entity_result: Dict
    ) -> Dict:

        try:

            # ----------------------------------------------------------
            # Companies
            # ----------------------------------------------------------

            companies = entity_result.get("companies", [])

            company_names = [
                company["company_name"]
                for company in companies
            ]

            company_symbols = [
                company["symbol"]
                for company in companies
            ]

            # ----------------------------------------------------------
            # Primary Company
            # ----------------------------------------------------------

            primary_symbol = (
                company_symbols[0]
                if company_symbols
                else None
            )

            primary_company = (
                company_names[0]
                if company_names
                else None
            )

            # ----------------------------------------------------------
            # Other Entities
            # ----------------------------------------------------------

            market_index = entity_result.get("market_index")
            sector = entity_result.get("sector")
            sentiment = entity_result.get("sentiment")
            time_filter = entity_result.get("time_filter")

            # ==========================================================
            # Retrieval Filters
            # ==========================================================

            filters = {

                "topic": (
                    market_index
                    if market_index
                    else primary_company
                ),

                "news_type": (
                    "INDEX"
                    if market_index
                    else (
                        "COMPANY"
                        if primary_company
                        else None
                    )
                ),

                "sentiment": sentiment,

                "source": None,

                "published_after": None,

                "published_before": None,

            }

            # ==========================================================
            # Final Formatted Output
            # ==========================================================

            formatted = {

                # ------------------------------------------------------
                # Original Query
                # ------------------------------------------------------

                "query": query,

                # ------------------------------------------------------
                # Intent
                # ------------------------------------------------------

                "intent": intent_result.get("intent"),

                "confidence": intent_result.get(
                    "confidence",
                    0.0
                ),

                # ------------------------------------------------------
                # Primary Company (NEW)
                # ------------------------------------------------------

                "symbol": primary_symbol,

                "company_name": primary_company,

                # ------------------------------------------------------
                # Entities
                # ------------------------------------------------------

                "companies": companies,

                "company_symbols": company_symbols,

                "company_names": company_names,

                "market_index": market_index,

                "sector": sector,

                "sentiment": sentiment,

                "time_filter": time_filter,

                # ------------------------------------------------------
                # Retrieval Filters
                # ------------------------------------------------------

                "filters": filters,

                # ------------------------------------------------------
                # Metadata
                # ------------------------------------------------------

                "metadata": {

                    "company_count": len(companies),

                    "generated_at": datetime.utcnow().isoformat(),

                    "version": "3.1"

                }

            }

            logger.info("Query formatting completed successfully.")

            logger.info(
                "Primary Company : %s (%s)",
                primary_company,
                primary_symbol
            )

            return formatted

        except Exception as e:

            logger.exception("Formatting failed.")

            raise QueryFormattingError(str(e))