"""
==============================================================================
Query Analyzer Exceptions
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System
Description : Custom exceptions for Query Analyzer V2
==============================================================================

"""


# ==============================================================================
# BASE EXCEPTION
# ==============================================================================

class QueryAnalyzerError(Exception):
    """
    Base exception for all Query Analyzer errors.
    """

    def __init__(self, message: str = "Query Analyzer Error"):

        super().__init__(message)


# ==============================================================================
# QUERY VALIDATION
# ==============================================================================

class InvalidQueryError(QueryAnalyzerError):
    """
    Raised when the user query is invalid.
    """

    def __init__(self, message="Invalid or empty query."):

        super().__init__(message)


# ==============================================================================
# INTENT CLASSIFIER
# ==============================================================================

class IntentClassificationError(QueryAnalyzerError):
    """
    Raised when intent classification fails.
    """

    def __init__(self, message="Unable to classify query intent."):

        super().__init__(message)


# ==============================================================================
# ENTITY EXTRACTION
# ==============================================================================

class EntityExtractionError(QueryAnalyzerError):
    """
    Raised when entity extraction fails.
    """

    def __init__(self, message="Unable to extract entities from query."):

        super().__init__(message)


# ==============================================================================
# DATABASE
# ==============================================================================

class DatabaseConnectionError(QueryAnalyzerError):
    """
    Raised when database connection fails.
    """

    def __init__(self, message="Database connection failed."):

        super().__init__(message)


class CompanyLoadingError(QueryAnalyzerError):
    """
    Raised when company data cannot be loaded.
    """

    def __init__(self, message="Unable to load companies from symbol_master."):

        super().__init__(message)


# ==============================================================================
# FORMATTER
# ==============================================================================

class QueryFormattingError(QueryAnalyzerError):
    """
    Raised when formatting of the analyzed query fails.
    """

    def __init__(self, message="Unable to format analyzed query."):

        super().__init__(message)


# ==============================================================================
# TIME PARSER
# ==============================================================================

class TimeParsingError(QueryAnalyzerError):
    """
    Raised when time parsing fails.
    """

    def __init__(self, message="Unable to parse time expression."):

        super().__init__(message)


# ==============================================================================
# SENTIMENT PARSER
# ==============================================================================

class SentimentDetectionError(QueryAnalyzerError):
    """
    Raised when sentiment detection fails.
    """

    def __init__(self, message="Unable to detect sentiment."):

        super().__init__(message)