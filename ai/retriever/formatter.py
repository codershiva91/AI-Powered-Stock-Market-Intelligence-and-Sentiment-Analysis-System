"""
=========================================================
Retriever Result Formatter
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Formats raw Qdrant search results into a clean,
consistent Python dictionary structure.

Responsibilities
----------------
1. Format a single search result
2. Format multiple search results
3. Standardize payload fields
4. Preserve similarity score

=========================================================
"""

from typing import List


class ResultFormatter:
    """
    Formats Qdrant search results.
    """

    # =====================================================

    @staticmethod
    def format_result(point):
        """
        Format a single Qdrant ScoredPoint.

        Parameters
        ----------
        point : ScoredPoint

        Returns
        -------
        dict
        """

        payload = point.payload or {}

        return {

            "news_id": payload.get("news_id"),

            "score": round(point.score, 4),

            "title": payload.get("title"),

            "document": payload.get("document"),

            "topic": payload.get("topic"),

            "source": payload.get("source"),

            "news_type": payload.get("news_type"),

            "sentiment": payload.get("sentiment"),

            "confidence_score": payload.get("confidence_score"),

            "published_at": payload.get("published_at"),
        }

    # =====================================================

    @staticmethod
    def format_results(points) -> List[dict]:
        """
        Format multiple search results.

        Parameters
        ----------
        points : list[ScoredPoint]

        Returns
        -------
        list[dict]
        """

        return [
            ResultFormatter.format_result(point)
            for point in points
        ]