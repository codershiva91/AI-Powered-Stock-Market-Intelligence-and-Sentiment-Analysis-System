"""
=========================================================
Payload Validation Module
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Validates payload quality stored in the Qdrant collection.

Responsibilities
----------------
1. Validate required payload fields
2. Detect missing fields
3. Detect empty fields
4. Validate document completeness
5. Generate payload summary

=========================================================
"""


class PayloadValidator:
    """
    Validates payload completeness stored in Qdrant.
    """

    REQUIRED_FIELDS = [
        "news_id",
        "title",
        "document",
        "source",
        "topic",
        "published_at",
        "news_type",
        "sentiment",
        "confidence_score"
    ]

    # =====================================================

    def __init__(self, points):
        self.points = points

    # =====================================================

    @staticmethod
    def _payload(point):
        """Safely return payload."""
        return point.payload or {}

    # =====================================================

    def validate(self):
        """
        Validate every payload field.
        """

        report = {}

        total = len(self.points)
        report["total_vectors"] = total

        for field in self.REQUIRED_FIELDS:

            missing = 0
            empty = 0

            for point in self.points:

                value = self._payload(point).get(field)

                if value is None:
                    missing += 1
                    continue

                if isinstance(value, str) and value.strip() == "":
                    empty += 1

            report[field] = {
                "missing": missing,
                "empty": empty,
                "valid": total - missing - empty
            }

        return report

    # =====================================================

    def _missing_string_field(self, field_name):
        """
        Count missing or empty string fields.
        """

        count = 0

        for point in self.points:

            value = self._payload(point).get(field_name)

            if value is None:
                count += 1
                continue

            if isinstance(value, str) and value.strip() == "":
                count += 1

        return count

    # =====================================================

    def empty_documents(self):
        return self._missing_string_field("document")

    # =====================================================

    def missing_titles(self):
        return self._missing_string_field("title")

    # =====================================================

    def missing_topics(self):
        return self._missing_string_field("topic")

    # =====================================================

    def missing_sources(self):
        return self._missing_string_field("source")

    # =====================================================

    def missing_sentiments(self):
        return self._missing_string_field("sentiment")

    # =====================================================

    def missing_dates(self):

        count = 0

        for point in self.points:

            date = self._payload(point).get("published_at")

            if date is None:
                count += 1

        return count

    # =====================================================

    def summary(self):
        """
        Overall payload validation summary.
        """

        return {
            "Empty Documents": self.empty_documents(),
            "Missing Titles": self.missing_titles(),
            "Missing Topics": self.missing_topics(),
            "Missing Sources": self.missing_sources(),
            "Missing Sentiments": self.missing_sentiments(),
            "Missing Dates": self.missing_dates(),
        }