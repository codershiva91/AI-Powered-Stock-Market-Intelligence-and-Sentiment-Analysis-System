"""
Custom exceptions for Semantic Search.
"""


class SemanticSearchError(Exception):
    """
    Base exception for semantic search.
    """
    pass


class EmptyQueryError(SemanticSearchError):
    """
    Raised when the search query is empty.
    """
    pass


class EmbeddingGenerationError(SemanticSearchError):
    """
    Raised when embedding generation fails.
    """
    pass


class QdrantSearchError(SemanticSearchError):
    """
    Raised when Qdrant search fails.
    """
    pass


class NoResultsFoundError(SemanticSearchError):
    """
    Raised when no similar documents are found.
    """
    pass


"""
exceptions.py
==============

Custom exception classes for the Semantic Search module.

Author : Shivam Sahu
Project: AI-Driven Stock Market Intelligence System
"""


class SemanticSearchError(Exception):
    """
    Base exception for all Semantic Search errors.
    """

    def __init__(self, message="Semantic Search Error"):
        super().__init__(message)


class EmptyQueryError(SemanticSearchError):
    """
    Raised when the user provides an empty search query.
    """

    def __init__(self):
        super().__init__("Search query cannot be empty.")


class EmbeddingGenerationError(SemanticSearchError):
    """
    Raised when the embedding model fails to generate an embedding.
    """

    def __init__(self, message="Failed to generate query embedding."):
        super().__init__(message)


class QdrantSearchError(SemanticSearchError):
    """
    Raised when Qdrant search fails.
    """

    def __init__(self, message="Qdrant search failed."):
        super().__init__(message)


class NoResultsFoundError(SemanticSearchError):
    """
    Raised when no semantic search results are found.
    """

    def __init__(self):
        super().__init__("No matching documents found.")