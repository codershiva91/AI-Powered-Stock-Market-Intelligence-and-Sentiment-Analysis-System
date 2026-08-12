"""
=========================================================
Vector Statistics Module
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Computes statistical information about vectors stored
in the Qdrant collection.

Responsibilities
----------------
- Total vector count
- Source distribution
- Topic distribution
- News type distribution
- Sentiment distribution
- Publication year distribution
- Document length statistics
=========================================================
"""

from collections import Counter
from datetime import datetime
from statistics import median


class VectorStatistics:
    """
    Computes statistics from Qdrant payloads.
    """

    def __init__(self, points):
        self.points = points

    # =====================================================

    @staticmethod
    def _payload(point):
        """
        Safely return payload.
        """
        return point.payload or {}

    # =====================================================

    def _distribution(self, field_name, default="Unknown", top_n=None):
        """
        Generic distribution calculator.

        Parameters
        ----------
        field_name : str
            Payload field name.

        default : str
            Default value for missing fields.

        top_n : int | None
            Return only top N values.
        """

        counter = Counter()

        for point in self.points:

            payload = self._payload(point)

            value = payload.get(field_name, default)

            if value in (None, ""):
                value = default

            counter[str(value)] += 1

        if top_n:
            return dict(counter.most_common(top_n))

        return dict(counter.most_common())

    # =====================================================

    def total_vectors(self):
        """
        Returns total vectors.
        """
        return len(self.points)

    # =====================================================

    def source_distribution(self, top_n=None):
        return self._distribution("source", top_n=top_n)

    # =====================================================

    def topic_distribution(self, top_n=None):
        return self._distribution("topic", top_n=top_n)

    # =====================================================

    def news_type_distribution(self):
        return self._distribution("news_type")

    # =====================================================

    def sentiment_distribution(self):
        return self._distribution("sentiment")

    # =====================================================

    def year_distribution(self):
        """
        Returns publication year distribution.
        """

        counter = Counter()

        for point in self.points:

            payload = self._payload(point)

            published_at = payload.get("published_at")

            if not published_at:
                counter["Unknown"] += 1
                continue

            try:

                year = datetime.fromisoformat(
                    str(published_at)
                ).year

                counter[str(year)] += 1

            except Exception:

                counter["Unknown"] += 1

        return dict(counter.most_common())

    # =====================================================

    def document_length_distribution(self):
        """
        Returns document length statistics.
        """

        lengths = []

        empty_documents = 0

        for point in self.points:

            payload = self._payload(point)

            document = payload.get("document", "")

            words = len(document.split())

            lengths.append(words)

            if words == 0:
                empty_documents += 1

        if not lengths:

            return {

                "average_words": 0,

                "median_words": 0,

                "minimum_words": 0,

                "maximum_words": 0,

                "empty_documents": 0

            }

        return {

            "average_words": round(sum(lengths) / len(lengths), 2),

            "median_words": median(lengths),

            "minimum_words": min(lengths),

            "maximum_words": max(lengths),

            "empty_documents": empty_documents

        }

    # =====================================================

    def summary(self):
        """
        Returns a summary of all statistics.
        """

        return {

            "Total Vectors": self.total_vectors(),

            "Source Distribution": self.source_distribution(),

            "Topic Distribution": self.topic_distribution(),

            "News Type Distribution": self.news_type_distribution(),

            "Sentiment Distribution": self.sentiment_distribution(),

            "Year Distribution": self.year_distribution(),

            "Document Length": self.document_length_distribution()

        }