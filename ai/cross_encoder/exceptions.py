"""
=========================================================
Cross Encoder Exceptions
=========================================================
"""


class CrossEncoderError(Exception):
    """Base exception for Cross Encoder."""
    pass


class ModelLoadError(CrossEncoderError):
    """Raised when model loading fails."""
    pass


class RerankingError(CrossEncoderError):
    """Raised during reranking."""
    pass