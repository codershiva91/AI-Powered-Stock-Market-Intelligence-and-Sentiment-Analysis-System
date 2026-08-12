"""
=========================================================
Semantic Retriever
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Semantic Retriever using Sentence Transformer
and Qdrant Vector Database.

Responsibilities
----------------
1. Process user query
2. Generate query embedding
3. Apply metadata filters
4. Perform semantic search
5. Format retrieved results

=========================================================
"""

from typing import Optional, List

from ai.sentence_transformer_embeddings.embedding_model import (
    generate_embedding,
)

from ai.sentence_transformer_embeddings.qdrant_manager import (
    QdrantManager,
)

from ai.retriever.config import (
    TOP_K,
)

from ai.retriever.filters import (
    SearchFilters,
)

from ai.retriever.query_processor import (
    QueryProcessor,
)

from ai.retriever.formatter import (
    ResultFormatter,
)

from ai.retriever.logger import (
    get_logger,
)

from ai.retriever.exceptions import (
    EmptyQueryError,
    RetrievalError,
)


class Retriever:
    """
    Semantic Retriever using Sentence Transformer
    and Qdrant Vector Database.
    """

    ##################################################################

    def __init__(self):

        self.logger = get_logger(__name__)

        self.qdrant = QdrantManager()

        self.logger.info("Retriever initialized successfully.")

    ##################################################################

    def search(
        self,
        query: str,
        top_k: int = TOP_K,
        topic: Optional[str] = None,
        sentiment: Optional[str] = None,
        news_type: Optional[str] = None,
        source: Optional[str] = None,
        published_after: Optional[str] = None,
        published_before: Optional[str] = None,
    ) -> List[dict]:
        """
        Perform semantic search.
        """

        # ------------------------------------------------------
        # Validate Query
        # ------------------------------------------------------

        if not query or not query.strip():
            raise EmptyQueryError("Search query cannot be empty.")

        try:

            # --------------------------------------------------
            # Query Processing
            # --------------------------------------------------

            processed_query = QueryProcessor.process(query)

            self.logger.info(
                f"Processed Query : {processed_query}"
            )

            # --------------------------------------------------
            # Generate Embedding
            # --------------------------------------------------

            query_vector = generate_embedding(processed_query)

            # --------------------------------------------------
            # Build Metadata Filters
            # --------------------------------------------------

            query_filter = SearchFilters.build(
                topic=topic,
                sentiment=sentiment,
                news_type=news_type,
                source=source,
                published_after=published_after,
                published_before=published_before,
            )

            # --------------------------------------------------
            # Vector Search
            # --------------------------------------------------

            results = self.qdrant.search(
                query_vector=query_vector,
                limit=top_k,
                query_filter=query_filter,
            )

            self.logger.info(
                f"{len(results)} documents retrieved."
            )

            # --------------------------------------------------
            # DEBUG : Print Raw Qdrant Payload
            # --------------------------------------------------

            print("\n" + "=" * 80)
            print("RAW QDRANT PAYLOAD")
            print("=" * 80)

            if not results:
                print("No results returned from Qdrant.")
            else:
                for i, point in enumerate(results[:2], start=1):
                    print(f"\nPoint {i}")
                    print(point.payload)
                    print("-" * 80)

            # --------------------------------------------------
            # Format Results
            # --------------------------------------------------

            formatted_results = ResultFormatter.format_results(
                results
            )

            return formatted_results

        except Exception as e:

            self.logger.exception(
                "Retriever search failed."
            )

            raise RetrievalError(str(e))

    ##################################################################

    def search_without_filters(
        self,
        query: str,
        top_k: int = TOP_K,
    ) -> List[dict]:
        """
        Perform semantic search without metadata filters.
        """

        return self.search(
            query=query,
            top_k=top_k,
        )