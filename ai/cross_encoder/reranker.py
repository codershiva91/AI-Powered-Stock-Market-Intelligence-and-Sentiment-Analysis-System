"""
==============================================================================
Cross Encoder Reranker
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Re-ranks retrieved documents using a Cross Encoder model.

Responsibilities
----------------
1. Load Cross Encoder model
2. Score retrieved documents
3. Sort documents by relevance
4. Return Top-K ranked documents

==============================================================================
"""

from typing import List, Dict

from sentence_transformers import CrossEncoder

from .logger import get_logger
from .exceptions import RerankingError

logger = get_logger(__name__)


class CrossEncoderReranker:
    """
    Cross Encoder based document reranker.
    """

    def __init__(
        self,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
    ):

        try:
            logger.info("Loading Cross Encoder model...")

            self.model = CrossEncoder(model_name)

            logger.info("Cross Encoder loaded successfully.")

        except Exception as e:
            logger.exception("Failed to load Cross Encoder model.")
            raise RerankingError(f"Model loading failed: {e}")

    ###########################################################################

    def rerank(
        self,
        query: str,
        documents: List[Dict],
        top_k: int = 5,
    ) -> List[Dict]:

        try:

            if not documents:
                logger.warning("No documents received for reranking.")
                return []

            sentence_pairs = []

            for doc in documents:

                text = (
                    doc.get("article_text")
                    or doc.get("content")
                    or doc.get("title")
                    or ""
                )

                sentence_pairs.append((query, text))

            scores = self.model.predict(sentence_pairs)

            for doc, score in zip(documents, scores):
                doc["rerank_score"] = float(score)

            documents.sort(
                key=lambda x: x["rerank_score"],
                reverse=True,
            )

            logger.info(
                "Successfully reranked %d documents.",
                len(documents),
            )

            return documents[:top_k]

        except Exception as e:

            logger.exception("Cross Encoder reranking failed.")

            raise RerankingError(str(e))