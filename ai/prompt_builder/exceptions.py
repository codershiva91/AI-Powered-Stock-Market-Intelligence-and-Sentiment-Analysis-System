"""
=========================================================
Prompt Builder Exceptions
=========================================================
"""


class PromptBuilderError(Exception):
    """Base exception."""


class EmptyContextError(PromptBuilderError):
    """Raised when context is empty."""


class EmptyQuestionError(PromptBuilderError):
    """Raised when user question is empty."""