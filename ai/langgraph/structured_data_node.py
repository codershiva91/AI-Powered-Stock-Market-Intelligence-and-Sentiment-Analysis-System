"""
==============================================================================
Structured Data Node
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Fetches structured financial data from MariaDB.

Responsibilities
----------------
1. Extract company symbol from Query Analyzer output.
2. Fetch latest stock price.
3. Fetch technical indicators.
4. Fetch company fundamentals.
5. Fetch aggregated company sentiment.
6. Store structured data in GraphState.

==============================================================================
"""

from ai.common.logger import get_logger
from ai.langgraph.state import GraphState
from database.stock_repository import StockRepository

logger = get_logger(__name__)


class StructuredDataNode:
    """
    LangGraph node responsible for fetching
    structured financial data from MariaDB.
    """

    def __init__(self):

        self.repository = StockRepository()

    ##########################################################################

    def __call__(self, state: GraphState) -> GraphState:

        logger.info("=" * 60)
        logger.info("STRUCTURED DATA NODE")
        logger.info("=" * 60)

        try:

            # ----------------------------------------------------------
            # Query Analysis
            # ----------------------------------------------------------

            analysis = state.get("query_analysis", {})

            logger.info("Query Analysis : %s", analysis)

            # ----------------------------------------------------------
            # Extract Symbol
            # ----------------------------------------------------------

            symbol = analysis.get("symbol")

            # Backward Compatibility
            if not symbol:

                company_symbols = analysis.get("company_symbols", [])

                if company_symbols:
                    symbol = company_symbols[0]

            # ----------------------------------------------------------
            # Symbol Not Found
            # ----------------------------------------------------------

            if not symbol:

                logger.warning("No stock symbol found in query analysis.")

                state["stock_data"] = {}
                state["technical_data"] = {}
                state["fundamental_data"] = {}
                state["sentiment_data"] = {}

                return state

            logger.info("Detected Symbol : %s", symbol)

            # ----------------------------------------------------------
            # Latest Stock Price
            # ----------------------------------------------------------

            stock_data = self.repository.get_latest_price(symbol)

            if stock_data:

                logger.info("Latest stock price retrieved.")

            else:

                logger.warning("No latest stock price found.")

                stock_data = {}

            # ----------------------------------------------------------
            # Technical Indicators
            # ----------------------------------------------------------

            technical_data = self.repository.get_technical_indicators(symbol)

            if technical_data:

                logger.info("Technical indicators retrieved.")

            else:

                logger.warning("No technical indicators found.")

                technical_data = {}

            # ----------------------------------------------------------
            # Company Fundamentals
            # ----------------------------------------------------------

            fundamental_data = self.repository.get_company_fundamentals(symbol)

            if fundamental_data:

                logger.info("Company fundamentals retrieved.")

            else:

                logger.warning("No company fundamentals found.")

                fundamental_data = {}

            # ----------------------------------------------------------
            # Company Sentiment
            # ----------------------------------------------------------

            sentiment_data = self.repository.get_company_sentiment(symbol)

            if sentiment_data:

                logger.info("Company sentiment retrieved.")

            else:

                logger.warning("No company sentiment found.")

                sentiment_data = {}

            # ----------------------------------------------------------
            # Update GraphState
            # ----------------------------------------------------------

            state["stock_data"] = stock_data

            state["technical_data"] = technical_data

            state["fundamental_data"] = fundamental_data

            state["sentiment_data"] = sentiment_data

            logger.info("Structured data successfully added to GraphState.")

            return state

        except Exception as e:

            logger.exception("Structured Data Node failed.")

            state["error"] = str(e)

            return state