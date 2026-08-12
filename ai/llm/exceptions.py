"""
=========================================================
LLM Exceptions
=========================================================
"""


class LLMError(Exception):
    """Base Exception"""


class GeminiConnectionError(LLMError):
    """Gemini Connection Error"""


class InvalidAPIKeyError(LLMError):
    """Invalid API Key"""


class GenerationError(LLMError):
    """LLM Generation Error"""