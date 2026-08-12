"""
=========================================================
Retriever Exceptions
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System
=========================================================
"""


class RetrieverError(Exception):
    """Base Retriever Exception."""
    pass


class EmptyQueryError(RetrieverError):
    """Raised when query is empty."""
    pass


class EmbeddingGenerationError(RetrieverError):
    """Raised when embedding generation fails."""
    pass


class RetrievalError(RetrieverError):
    """Raised when Qdrant search fails."""
    pass


class InvalidFilterError(RetrieverError):
    """Raised when metadata filters are invalid."""
    pass