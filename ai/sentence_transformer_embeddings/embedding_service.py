"""
=========================================================
Embedding Service
Sentence Transformer Embedding Module

Author : Shivam Sahu
Project : AI Stock Market Intelligence System
=========================================================

This module:     

1. Cleans news articles
2. Generates Sentence Transformer embeddings
3. Creates Qdrant PointStruct objects
4. Prepares metadata payload

=========================================================
"""

from qdrant_client.http.models import PointStruct

from .preprocess import (
    prepare_document,
    is_valid_document
)

from .embedding_model import generate_embedding

from .logger import get_logger

logger = get_logger(__name__)


class EmbeddingService:
    """
    Business logic for converting
    news articles into Qdrant vectors.
    """

    def __init__(self):  
        logger.info("Embedding Service Initialized")

#====================================================

    def create_payload(self, news_row, document):
        """
        Create metadata payload.

        Parameters
        ----------
        news_row : dict

        document : str

        Returns
        -------
        dict
        """

        payload = {

            "news_id": news_row["news_id"],

            "title": news_row["title"],

            "document": document,

            "source": news_row.get("source"),

            "topic": news_row.get("topic"),

            "news_type": news_row.get("news_type"),

            "published_at": (
                str(news_row["published_at"])
                if news_row["published_at"]
                else None
            ),

            "sentiment": news_row.get("sentiment"),

            "confidence_score": (
                float(news_row["confidence_score"])
                if news_row["confidence_score"] is not None
                else None
            )

        }

        return payload

    # =========================================================

    def process_news(self, news_row):
        """
        Convert one news record into
        a Qdrant PointStruct.

        Parameters
        ----------
        news_row : dict

        Returns
        -------
        PointStruct | None
        """

        try:

            document = prepare_document(

                news_row["title"],

                news_row["article_text"]

            )

            if not is_valid_document(document):

                logger.warning(
                    f"Skipping News ID {news_row['news_id']} "
                    "(Invalid Document)"
                )

                return None

            embedding = generate_embedding(document)

            payload = self.create_payload(

                news_row,

                document

            )

            point = PointStruct(

                id=int(news_row["news_id"]),

                vector=embedding,

                payload=payload

            )

            return point

        except Exception as error:

            logger.exception(

                f"Embedding failed "
                f"(News ID {news_row['news_id']})"

            )

            return None