"""
==============================================================================
Project Exceptions
==============================================================================

Shared exception classes for the AI-Driven Stock Market Intelligence System.
==============================================================================
"""


class AIProjectError(Exception):
    """Base exception for the project."""


class ConfigurationError(AIProjectError):
    """Configuration related errors."""


class DatabaseError(AIProjectError):
    """Database related errors."""


class RetrievalError(AIProjectError):
    """Retriever related errors."""


class LLMError(AIProjectError):
    """LLM related errors."""


class AgentError(AIProjectError):
    """Agent related errors."""