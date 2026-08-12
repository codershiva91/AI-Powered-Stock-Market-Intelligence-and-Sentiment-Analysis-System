"""
==============================================================================
News AI Agent
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
News Agent responsible for handling stock market news related queries.

This agent delegates all AI processing to the LangGraph workflow.

Workflow
--------
User Question
      │
      ▼
NewsAgent
      │
      ▼
LangGraph
      │
      ▼
Final Response

==============================================================================
"""

from ai.common.logger import get_logger
from ai.common.exceptions import AgentError

from ai.langgraph.graph import graph
from ai.langgraph.state_factory import create_graph_state


logger = get_logger(__name__)


# =============================================================================
# News Agent
# =============================================================================

class NewsAgent:
    """
    AI Agent for handling news-related queries.
    """

    def __init__(self) -> None:
        """
        Initialize the News Agent.
        """
        logger.info("NewsAgent initialized.")

    # -------------------------------------------------------------------------

    def run(self, question: str) -> str:
        """
        Process a news-related user question.

        Parameters
        ----------
        question : str
            User question.

        Returns
        -------
        str
            AI generated response.
        """

        logger.info(f"NewsAgent received question: {question}")

        try:

            # Create initial LangGraph state
            state = create_graph_state(question)

            # Execute LangGraph workflow
            result = graph.invoke(state)

            logger.info("NewsAgent completed successfully.")

            return result.get(
                "response",
                "No response generated."
            )

        except Exception as e:

            logger.exception("NewsAgent execution failed.")

            raise AgentError(
                f"NewsAgent Error: {str(e)}"
            ) from e