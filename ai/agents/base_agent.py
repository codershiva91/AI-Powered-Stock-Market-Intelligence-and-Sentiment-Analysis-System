"""
==============================================================================
Base AI Agent
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Base class for all AI Agents.

Responsibilities
----------------
1. Create LangGraph state
2. Execute LangGraph workflow
3. Validate inputs
4. Handle logging
5. Handle exceptions

==============================================================================
"""

from abc import ABC

from ai.common.logger import get_logger
from ai.common.exceptions import AgentError

from ai.langgraph.graph import graph
from ai.langgraph.state_factory import create_graph_state


class BaseAgent(ABC):
    """
    Base class for all AI Agents.
    """

    ##################################################################

    def __init__(self):

        self.logger = get_logger(self.__class__.__name__)

        self.logger.info(
            "%s initialized.",
            self.__class__.__name__
        )

    ##################################################################

    def create_state(self, question: str):
        """
        Create the initial LangGraph state.
        """

        return create_graph_state(question)

    ##################################################################

    def invoke_graph(self, question: str) -> str:
        """
        Execute LangGraph.

        Parameters
        ----------
        question : str

        Returns
        -------
        str
        """

        self.logger.info("=" * 80)
        self.logger.info("BASE AGENT")
        self.logger.info("=" * 80)

        self.logger.info(
            "Question Type : %s",
            type(question).__name__
        )

        self.logger.info(
            "Question : %s",
            question
        )

        # ----------------------------------------------------------
        # Validate Input
        # ----------------------------------------------------------

        if not isinstance(question, str):

            raise TypeError(
                f"Expected question to be str, "
                f"received {type(question).__name__}"
            )

        if not question.strip():

            raise ValueError(
                "Question cannot be empty."
            )

        try:

            # ------------------------------------------------------
            # Create Initial Graph State
            # ------------------------------------------------------

            state = self.create_state(question)

            self.logger.info(
                "Graph state created successfully."
            )

            # ------------------------------------------------------
            # Execute LangGraph
            # ------------------------------------------------------

            result = graph.invoke(state)

            self.logger.info(
                "Graph execution completed successfully."
            )

            response = result.get(
                "response",
                "No response generated."
            )

            self.logger.info(
                "Response generated (%d characters).",
                len(response)
            )

            return response

        except Exception as e:

            self.logger.exception(
                "Graph execution failed."
            )

            raise AgentError(
                f"{self.__class__.__name__}: {str(e)}"
            ) from e