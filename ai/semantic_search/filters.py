"""
filters.py
==========

Provides metadata filtering utilities for Semantic Search results.

Author : Shivam Sahu
Project: AI-Driven Stock Market Intelligence System
"""

from typing import List, Dict, Optional


class SearchFilters:
    """
    Utility class for filtering semantic search results.
    """

    @staticmethod
    def filter_results(
        results: List[Dict],
        sentiment: Optional[str] = None,
        source: Optional[str] = None,
        topic: Optional[str] = None,
        news_type: Optional[str] = None,
        symbol: Optional[str] = None,
    ) -> List[Dict]:
        """
        Filter search results based on metadata.

        Parameters
        ----------
        results : List[Dict]
            Search results returned by Semantic Search.

        sentiment : str, optional
            Positive / Neutral / Negative

        source : str, optional
            News source

        topic : str, optional
            News topic

        news_type : str, optional
            MARKET / COMPANY / INDEX / GENERAL / SECTOR

        symbol : str, optional
            Stock symbol (future use)

        Returns
        -------
        List[Dict]
            Filtered results.
        """

        filtered = results

        if sentiment:
            filtered = [
                item for item in filtered
                if item.get("sentiment", "").lower() == sentiment.lower()
            ]

        if source:
            filtered = [
                item for item in filtered
                if item.get("source", "").lower() == source.lower()
            ]

        if topic:
            filtered = [
                item for item in filtered
                if item.get("topic", "").lower() == topic.lower()
            ]

        if news_type:
            filtered = [
                item for item in filtered
                if item.get("news_type", "").lower() == news_type.lower()
            ]

        if symbol:
            filtered = [
                item for item in filtered
                if item.get("symbol", "").upper() == symbol.upper()
            ]

        return filtered