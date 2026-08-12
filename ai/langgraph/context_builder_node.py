"""
=========================================================
LangGraph Context Builder Node
=========================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Builds a unified context for the LLM by combining:

1. Structured financial data from MariaDB
2. Technical indicators
3. Company fundamentals
4. Reranked news documents

The generated context is later consumed by the Prompt Builder
and Gemini.

=========================================================
"""

from ai.langgraph.state import GraphState

from ai.context_builder.builder import ContextBuilder
from ai.context_builder.logger import get_logger

logger = get_logger(__name__)


class ContextBuilderNode:
    """
    LangGraph node responsible for building
    the final LLM context.
    """

    ##################################################################

    def __init__(self):

        self.builder = ContextBuilder()

    ##################################################################

    def __call__(self, state: GraphState) -> GraphState:

        try:

            logger.info("=" * 60)
            logger.info("CONTEXT BUILDER NODE")
            logger.info("=" * 60)

            stock_data = state.get("stock_data", {})
            technical_data = state.get("technical_data", {})
            fundamental_data = state.get("fundamental_data", {})
            documents = state.get("reranked_documents", [])

            logger.info("Building final LLM context...")

            context_parts = []

            # ==========================================================
            # Latest Stock Data
            # ==========================================================

            if stock_data:

                context_parts.append(
                    "==============================\n"
                    "LATEST STOCK DATA\n"
                    "=============================="
                )

                for key, value in stock_data.items():
                    context_parts.append(f"{key}: {value}")

                context_parts.append("")

            # ==========================================================
            # Technical Indicators
            # ==========================================================

            if technical_data:

                context_parts.append(
                    "==============================\n"
                    "TECHNICAL INDICATORS\n"
                    "=============================="
                )

                for key, value in technical_data.items():
                    context_parts.append(f"{key}: {value}")

                context_parts.append("")

            # ==========================================================
            # Company Fundamentals
            # ==========================================================

            if fundamental_data:

                context_parts.append(
                    "==============================\n"
                    "COMPANY FUNDAMENTALS\n"
                    "=============================="
                )

                for key, value in fundamental_data.items():
                    context_parts.append(f"{key}: {value}")

                context_parts.append("")

            # ==========================================================
            # News Context
            # ==========================================================

            if documents:

                logger.info(
                    "Adding %d reranked documents.",
                    len(documents)
                )

                news_context = self.builder.build(documents)

                context_parts.append(
                    "==============================\n"
                    "RECENT NEWS\n"
                    "=============================="
                )

                context_parts.append(news_context)

            else:

                logger.warning("No reranked documents found.")

            # ==========================================================
            # Final Context
            # ==========================================================

            final_context = "\n".join(context_parts)

            state["context"] = final_context
            state["error"] = None

            logger.info(
                "Context built successfully (%d characters).",
                len(final_context)
            )

            return state

        except Exception as e:

            logger.exception("Context Builder Node failed.")

            state["context"] = ""
            state["error"] = str(e)

            return state