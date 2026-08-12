"""
==============================================================================
Query Analyzer Intent Classifier
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
Description : Priority-based intent classification for Query Analyzer V2
==============================================================================

"""

import re
from typing import Dict

from .config import (
    INTENT_PATTERNS,
    INTENT_PRIORITY,
    DEFAULT_INTENT
)

from .logger import get_logger
from .exceptions import (
    InvalidQueryError,
    IntentClassificationError
)

logger = get_logger(__name__)


class IntentClassifier:
    """
    Production-grade Intent Classifier.

    Responsibilities
    ----------------
    1. Normalize query
    2. Apply priority-based intent matching
    3. Calculate confidence score
    """

    def __init__(self):

        logger.info("Intent Classifier initialized.")

    # ======================================================================
    # NORMALIZE QUERY
    # ======================================================================

    @staticmethod
    def normalize(query: str) -> str:
        """
        Normalize user query.
        """

        if query is None:
            raise InvalidQueryError("Query cannot be None.")

        if not isinstance(query, str):
            raise InvalidQueryError("Query must be a string.")

        query = query.strip()

        if not query:
            raise InvalidQueryError("Query cannot be empty.")

        query = query.lower()

        query = re.sub(r"\s+", " ", query)

        return query

    # ======================================================================
    # CLASSIFY
    # ======================================================================

    def classify(self, query: str) -> Dict:
        """
        Classify query intent.

        Returns
        -------
        {
            "intent": "...",
            "confidence": 0.95
        }
        """

        try:

            normalized_query = self.normalize(query)

            logger.info("Intent Classification started.")

            # ==============================================================
            # SPECIAL RULES FOR COMPARISON QUERIES
            # ==============================================================

            comparison_patterns = [

                r"\bcompare\b",
                r"\bcomparison\b",
                r"\bvs\b",
                r"\bversus\b",
                r"\bdifference\b",
                r"\bbetter than\b",
                r"\bwhich is better\b",
                r"\bcompare with\b",
                r"\bagainst\b",
                r"\bcompare .* with\b",
                r"\bcompare .* and\b",
                r"\bor\b"

            ]

            for pattern in comparison_patterns:

                if re.search(pattern, normalized_query):

                    logger.info(
                        "Detected Intent: COMPARE_COMPANIES | Rule: %s",
                        pattern
                    )

                    return {

                        "intent": "COMPARE_COMPANIES",

                        "confidence": 0.90

                    }

            # ==============================================================
            # PRIORITY BASED MATCHING
            # ==============================================================

            for intent in INTENT_PRIORITY:

                if intent == DEFAULT_INTENT:
                    continue

                keywords = INTENT_PATTERNS.get(intent, [])

                matched = []

                for keyword in keywords:

                    pattern = rf"\b{re.escape(keyword.lower())}\b"

                    if re.search(pattern, normalized_query):

                        matched.append(keyword)

                if matched:

                    confidence = min(
                        0.60 + (0.10 * len(matched)),
                        0.99
                    )

                    logger.info(
                        "Detected Intent: %s | Matched: %s",
                        intent,
                        matched
                    )

                    return {

                        "intent": intent,

                        "confidence": round(confidence, 2)

                    }

            logger.info(
                "No intent matched. Using GENERAL_QUERY."
            )

            return {

                "intent": DEFAULT_INTENT,

                "confidence": 0.50

            }

        except InvalidQueryError:
            raise

        except Exception as e:

            logger.exception(
                "Intent Classification Failed."
            )

            raise IntentClassificationError(str(e))