"""
semantic_search.py
==================

Semantic Search Engine

Author : Shivam Sahu
Project: AI-Driven Stock Market Intelligence System
"""

from typing import List, Dict, Any

from ai.sentence_transformer_embeddings.embedding_model import generate_embedding
from ai.sentence_transformer_embeddings.qdrant_manager import QdrantManager
from ai.sentence_transformer_embeddings.logger import get_logger

from .exceptions import (
    EmptyQueryError,
    EmbeddingGenerationError,
    QdrantSearchError,
)

logger = get_logger(__name__)


class SemanticSearch:
    """
    Semantic Search Engine

    Workflow:
        User Query
            ↓
        Generate Embedding
            ↓
        Search Qdrant
            ↓
        Normalize Payload
            ↓
        Return Search Results
    """

    def __init__(self):

        self.qdrant = QdrantManager()

    @staticmethod
    def _extract_document(payload: Dict[str, Any]) -> str:
        """
        Extract document text from different payload formats.

        Supports multiple payload schemas.
        """

        candidate_fields = [
            "article_text",
            "document",
            "content",
            "text",
            "description",
            "summary",
            "body",
            "comment",
            "message",
        ]

        for field in candidate_fields:

            value = payload.get(field)

            if value:
                return str(value)

        return "Document not available."

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> List[Dict]:
        """
        Perform semantic search.

        Parameters
        ----------
        query : str
            User search query

        top_k : int
            Number of nearest neighbours

        Returns
        -------
        List[Dict]
        """

        if not query or not query.strip():
            raise EmptyQueryError()

        logger.info("Generating embedding for query...")

        try:

            query_vector = generate_embedding(query)

        except Exception as e:
            logger.exception("Embedding generation failed.")
            raise EmbeddingGenerationError(str(e))

        logger.info("Searching Qdrant...")

        try:

            search_results = self.qdrant.search(
                query_vector=query_vector,
                limit=top_k,
            )

        except Exception as e:
            logger.exception("Qdrant search failed.")
            raise QdrantSearchError(str(e))

        logger.info(
            "Retrieved %d semantic search results.",
            len(search_results),
        )

        results = []

        for hit in search_results:

            payload = hit.payload or {}

            results.append(
                {
                    "score": round(float(hit.score), 4),
                    "news_id": payload.get("news_id"),
                    "title": payload.get("title", "Untitled"),
                    "source": payload.get("source", "Unknown"),
                    "topic": payload.get("topic", "Unknown"),
                    "news_type": payload.get("news_type", "Unknown"),
                    "published_at": payload.get("published_at"),
                    "sentiment": payload.get("sentiment", "Unknown"),
                    "symbol": payload.get("symbol"),
                    "document": self._extract_document(payload),
                    "payload": payload,
                }
            )

        return results