"""
=========================================================
Prompt Formatter
=========================================================

Author : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Description:
Formats prompts for debugging and logging.
=========================================================
"""


class PromptFormatter:
    """
    Prompt Formatter
    """

    @staticmethod
    def format(prompt: str) -> str:

        if not prompt:
            return "No prompt generated."

        return (
            "\n"
            + "=" * 100
            + "\n"
            + " FINAL PROMPT\n"
            + "=" * 100
            + "\n\n"
            + prompt
            + "\n"
            + "=" * 100
        )