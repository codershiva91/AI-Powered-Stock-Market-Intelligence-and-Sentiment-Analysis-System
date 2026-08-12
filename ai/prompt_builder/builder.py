"""
=========================================================
Prompt Builder
=========================================================

Author : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Description:
Builds the final prompt for the LLM.
=========================================================
"""

from typing import Dict

from .config import (
    SYSTEM_ROLE,
    INSTRUCTIONS,
    INTENT_INSTRUCTIONS,
    OUTPUT_FORMAT,
)

from .exceptions import (
    EmptyContextError,
    EmptyQuestionError,
)

from .logger import get_logger


logger = get_logger(__name__)


class PromptBuilder:
    """
    Builds the final prompt for the LLM.
    """

    def __init__(self):

        logger.info("Prompt Builder initialized.")

    ##################################################################

    def build(
        self,
        question: str,
        context: str,
        query_analysis: Dict,
    ) -> str:
        """
        Build the final LLM prompt.

        Parameters
        ----------
        question : str
            User question.

        context : str
            Retrieved context.

        query_analysis : dict
            Output from Query Analyzer.

        Returns
        -------
        str
            Final prompt.
        """

        # --------------------------------------------------
        # Validation
        # --------------------------------------------------

        if not question or not question.strip():
            raise EmptyQuestionError(
                "Question cannot be empty."
            )

        if not context or not context.strip():
            raise EmptyContextError(
                "Context cannot be empty."
            )

        if query_analysis is None:
            query_analysis = {}

        logger.info("Building final prompt...")

        # --------------------------------------------------
        # Extract Query Analyzer Information
        # --------------------------------------------------

        intent = query_analysis.get("intent", "GENERAL_QUERY")

        companies = query_analysis.get("company_names", [])

        company_symbols = query_analysis.get("company_symbols", [])

        sector = query_analysis.get("sector")

        market_index = query_analysis.get("market_index")

        sentiment = query_analysis.get("sentiment")

        time_filter = query_analysis.get("time_filter")

        confidence = query_analysis.get("confidence")

        # --------------------------------------------------
        # Prompt
        # --------------------------------------------------

        prompt = f"""
{SYSTEM_ROLE}

============================================================
QUERY ANALYSIS
============================================================

Intent              : {intent}

Companies           : {', '.join(companies) if companies else 'None'}

Company Symbols     : {', '.join(company_symbols) if company_symbols else 'None'}

Sector              : {sector or 'None'}

Market Index        : {market_index or 'None'}

Sentiment           : {sentiment or 'None'}

Time Filter         : {time_filter or 'None'}

Confidence          : {confidence}

============================================================
USER QUESTION
============================================================

{question}

============================================================
RETRIEVED CONTEXT
============================================================

{context}

============================================================
TASK
============================================================

{
INTENT_INSTRUCTIONS.get(
    intent,
    INSTRUCTIONS
)
}

============================================================
OUTPUT FORMAT
============================================================

{OUTPUT_FORMAT}
"""

        logger.info(
            "Prompt built successfully (%d characters).",
            len(prompt)
        )

        return prompt