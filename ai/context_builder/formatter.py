"""
=========================================================
Context Formatter
=========================================================

Author : Shivam Sahu
Project: AI-Driven Stock Market Intelligence System

Description:
Formats the generated context for display or LLM.
=========================================================
"""


class ContextFormatter:
    """
    Context Formatter
    """

    @staticmethod
    def format(context: str) -> str:
        """
        Format context for readability.

        Parameters
        ----------
        context : str

        Returns
        -------
        str
        """

        if not context:
            return "No context generated."

        return (
            "\n"
            + "=" * 100
            + "\n"
            + " GENERATED CONTEXT\n"
            + "=" * 100
            + "\n\n"
            + context
            + "\n"
            + "=" * 100
        )