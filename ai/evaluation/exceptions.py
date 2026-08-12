"""
=========================================================
Evaluation Exceptions
=========================================================

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Description
-----------
Custom exceptions for the Evaluation module.

Responsibilities
----------------
1. Benchmark file errors
2. Evaluation execution errors
3. Metrics calculation errors
4. Report generation errors

=========================================================
"""


class EvaluationError(Exception):
    """
    Base exception for the Evaluation module.
    """
    pass


# =====================================================
# Benchmark Exceptions
# =====================================================

class BenchmarkFileNotFoundError(EvaluationError):
    """
    Raised when the benchmark dataset is missing.
    """
    pass


class InvalidBenchmarkFormatError(EvaluationError):
    """
    Raised when the benchmark JSON format is invalid.
    """
    pass


class EmptyBenchmarkError(EvaluationError):
    """
    Raised when the benchmark dataset contains no questions.
    """
    pass


# =====================================================
# Evaluation Exceptions
# =====================================================

class PipelineExecutionError(EvaluationError):
    """
    Raised when the RAG pipeline fails during evaluation.
    """
    pass


class MetricsCalculationError(EvaluationError):
    """
    Raised when evaluation metrics cannot be calculated.
    """
    pass


class ReportGenerationError(EvaluationError):
    """
    Raised when the evaluation report cannot be generated.
    """
    pass