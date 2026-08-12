"""
=========================================================
Context Builder Exceptions
=========================================================
"""


class ContextBuilderError(Exception):
    """Base exception."""


class EmptyDocumentsError(ContextBuilderError):
    """No documents received."""


class ContextFormattingError(ContextBuilderError):
    """Context formatting failed."""