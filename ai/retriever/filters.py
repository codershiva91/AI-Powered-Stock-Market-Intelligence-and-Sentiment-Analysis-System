"""
=========================================================
Qdrant Metadata Filters
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Builds metadata filters for semantic retrieval.

Responsibilities
----------------
1. Topic filtering
2. Sentiment filtering
3. News type filtering
4. Source filtering
5. Date filtering
6. Build Qdrant Filter object

=========================================================
"""

from typing import Optional

from qdrant_client.http.models import (
    Filter,
    FieldCondition,
    MatchValue,
    Range,
)


class SearchFilters:
    """
    Helper class to build Qdrant metadata filters.
    """

    @staticmethod
    def build(
        topic: Optional[str] = None,
        sentiment: Optional[str] = None,
        news_type: Optional[str] = None,
        source: Optional[str] = None,
        published_after: Optional[str] = None,
        published_before: Optional[str] = None,
    ) -> Optional[Filter]:
        """
        Build Qdrant filter object.

        Returns
        -------
        Filter | None
        """

        conditions = []

        # --------------------------------------------------
        # Topic
        # --------------------------------------------------

        if topic:

            conditions.append(
                FieldCondition(
                    key="topic",
                    match=MatchValue(value=topic)
                )
            )

        # --------------------------------------------------
        # Sentiment
        # --------------------------------------------------

        if sentiment:

            conditions.append(
                FieldCondition(
                    key="sentiment",
                    match=MatchValue(value=sentiment)
                )
            )

        # --------------------------------------------------
        # News Type
        # --------------------------------------------------

        if news_type:

            conditions.append(
                FieldCondition(
                    key="news_type",
                    match=MatchValue(value=news_type)
                )
            )

        # --------------------------------------------------
        # Source
        # --------------------------------------------------

        if source:

            conditions.append(
                FieldCondition(
                    key="source",
                    match=MatchValue(value=source)
                )
            )

        # --------------------------------------------------
        # Published After
        # --------------------------------------------------

        if published_after:

            conditions.append(
                FieldCondition(
                    key="published_at",
                    range=Range(
                        gte=published_after
                    )
                )
            )

        # --------------------------------------------------
        # Published Before
        # --------------------------------------------------

        if published_before:

            conditions.append(
                FieldCondition(
                    key="published_at",
                    range=Range(
                        lte=published_before
                    )
                )
            )

        if not conditions:
            return None

        return Filter(
            must=conditions
        )