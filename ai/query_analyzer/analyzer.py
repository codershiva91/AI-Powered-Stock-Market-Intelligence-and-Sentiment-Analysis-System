"""
==============================================================================
Query Analyzer
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
Description : Main orchestrator for Query Analyzer V2
==============================================================================

Responsibilities
----------------
1. Validate user query
2. Detect intent
3. Extract entities
4. Format response
5. Return structured analysis

==============================================================================
"""

from typing import Dict

from .intent import IntentClassifier
from .entities import EntityExtractor
from .formatter import QueryFormatter

from .logger import get_logger
from .exceptions import (
    InvalidQueryError,
    QueryAnalyzerError
)

logger = get_logger(__name__)


class QueryAnalyzer:
    """
    Main Query Analyzer.

    Example
    -------
    analyzer = QueryAnalyzer()

    result = analyzer.analyze(
        "Compare Reliance and Infosys this week"
    )
    """

    def __init__(self):

        logger.info("Initializing Query Analyzer...")

        self.intent_classifier = IntentClassifier()

        self.entity_extractor = EntityExtractor()

        self.formatter = QueryFormatter()

        logger.info("Query Analyzer initialized successfully.")

    # ======================================================================
    # VALIDATE QUERY
    # ======================================================================

    @staticmethod
    def validate_query(query: str):

        if query is None:
            raise InvalidQueryError("Query cannot be None.")

        if not isinstance(query, str):
            raise InvalidQueryError("Query must be a string.")

        query = query.strip()

        if len(query) == 0:
            raise InvalidQueryError("Query cannot be empty.")

        return query

    # ======================================================================
    # ANALYZE
    # ======================================================================

    def analyze(self, query: str) -> Dict:
        """
        Analyze user query.

        Parameters
        ----------
        query : str

        Returns
        -------
        dict
        """

        try:

            logger.info("Starting query analysis...")

            query = self.validate_query(query)

            # ----------------------------------------------------------
            # Intent Classification
            # ----------------------------------------------------------

            intent_result = self.intent_classifier.classify(query)

            logger.info(
                "Intent Detected : %s",
                intent_result["intent"]
            )

            # ----------------------------------------------------------
            # Entity Extraction
            # ----------------------------------------------------------

            entity_result = self.entity_extractor.extract(query)

            logger.info("Entities extracted successfully.")

            # ----------------------------------------------------------
            # Formatting
            # ----------------------------------------------------------

            formatted_result = self.formatter.format(

                query=query,

                intent_result=intent_result,

                entity_result=entity_result

            )

            logger.info("Query analysis completed successfully.")

            return formatted_result

        except QueryAnalyzerError:

            logger.exception("Query Analyzer failed.")

            raise

        except Exception as e:

            logger.exception("Unexpected Error.")

            raise QueryAnalyzerError(str(e))