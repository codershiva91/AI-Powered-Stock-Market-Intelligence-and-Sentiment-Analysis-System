"""
=========================================================
Evaluation Formatter
=========================================================

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Description
-----------
Formats evaluation results into a clean and
human-readable report.

Responsibilities
----------------
1. Format individual test results
2. Format summary statistics
3. Standardize console output

=========================================================
"""

from typing import Dict


class EvaluationFormatter:
    """
    Formats evaluation results.
    """

    LINE = "=" * 80

    @staticmethod
    def format_test(
        test_number: int,
        question: str,
        retrieved_docs: int,
        response_time: float,
        status: str,
    ) -> str:
        """
        Format a single evaluation result.
        """

        return f"""
{EvaluationFormatter.LINE}
Test #{test_number}
{EvaluationFormatter.LINE}

Question           : {question}

Retrieved Docs     : {retrieved_docs}

Response Time      : {response_time:.2f} sec

Status             : {status}

{EvaluationFormatter.LINE}
"""

    ##################################################################

    @staticmethod
    def format_summary(metrics: Dict) -> str:
        """
        Format evaluation summary.
        """

        return f"""
{EvaluationFormatter.LINE}
EVALUATION SUMMARY
{EvaluationFormatter.LINE}

Total Questions        : {metrics.get("total_questions", 0)}

Successful Queries     : {metrics.get("successful_queries", 0)}

Failed Queries         : {metrics.get("failed_queries", 0)}

Average Response Time  : {metrics.get("average_response_time", 0):.2f} sec

Retriever Accuracy     : {metrics.get("retriever_accuracy", 0):.2f} %

LLM Success Rate       : {metrics.get("llm_success_rate", 0):.2f} %

No Result Rate         : {metrics.get("no_result_rate", 0):.2f} %

{EvaluationFormatter.LINE}
"""