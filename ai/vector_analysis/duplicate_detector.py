"""
=========================================================
Duplicate Detection Module
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Detect duplicate records stored in the Qdrant collection.

Checks
------
1. Duplicate News IDs
2. Duplicate Titles
3. Duplicate Documents
4. Duplicate (Title + Document) pairs

=========================================================
"""

from collections import Counter
import hashlib


class DuplicateDetector:
    """
    Detect duplicate payloads stored in Qdrant.
    """

    # =====================================================

    def __init__(self, points):
        self.points = points

    # =====================================================

    @staticmethod
    def _payload(point):
        """Safely return payload."""
        return point.payload or {}

    # =====================================================

    @staticmethod
    def normalize(text):
        """
        Normalize text before comparison.
        """

        if text is None:
            return ""

        return " ".join(str(text).strip().lower().split())

    # =====================================================

    @staticmethod
    def generate_hash(text):
        """
        Generate SHA256 hash.
        """

        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    # =====================================================

    def duplicate_news_ids(self):

        counter = Counter()

        for point in self.points:

            news_id = self._payload(point).get("news_id")

            if news_id is not None:
                counter[news_id] += 1

        return {
            key: value
            for key, value in counter.items()
            if value > 1
        }

    # =====================================================

    def duplicate_titles(self):

        counter = Counter()

        for point in self.points:

            title = self.normalize(
                self._payload(point).get("title")
            )

            if title:
                counter[title] += 1

        return {
            key: value
            for key, value in counter.items()
            if value > 1
        }

    # =====================================================

    def duplicate_documents(self):

        counter = Counter()

        for point in self.points:

            document = self.normalize(
                self._payload(point).get("document")
            )

            if document:

                document_hash = self.generate_hash(document)

                counter[document_hash] += 1

        return {
            key: value
            for key, value in counter.items()
            if value > 1
        }

    # =====================================================

    def duplicate_title_document_pairs(self):

        counter = Counter()

        for point in self.points:

            payload = self._payload(point)

            title = self.normalize(
                payload.get("title")
            )

            document = self.normalize(
                payload.get("document")
            )

            combined = f"{title}|{document}"

            if combined.strip("|"):

                pair_hash = self.generate_hash(combined)

                counter[pair_hash] += 1

        return {
            key: value
            for key, value in counter.items()
            if value > 1
        }

    # =====================================================

    def summary(self):

        news_duplicates = self.duplicate_news_ids()

        title_duplicates = self.duplicate_titles()

        document_duplicates = self.duplicate_documents()

        pair_duplicates = self.duplicate_title_document_pairs()

        return {
            "Duplicate News IDs": len(news_duplicates),
            "Duplicate Titles": len(title_duplicates),
            "Duplicate Documents": len(document_duplicates),
            "Duplicate Title + Document": len(pair_duplicates),
        }