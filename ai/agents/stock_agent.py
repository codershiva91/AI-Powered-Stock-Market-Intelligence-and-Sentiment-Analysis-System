"""
==============================================================================
Stock AI Agent
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
AI Agent responsible for handling stock-related queries.
==============================================================================

"""

from ai.agents.base_agent import BaseAgent
from database.stock_repository import StockRepository


class StockAgent(BaseAgent):
    """
    Handles stock-related AI queries.
    """

    def __init__(self):

        super().__init__()

        self.repository = StockRepository()

    # ------------------------------------------------------------------

    def run(self, question: str) -> str:
        """
        Process stock-related query.

        Parameters
        ----------
        question : str

        Returns
        -------
        str
            AI generated response.
        """

        self.logger.info("=" * 80)
        self.logger.info("STOCK AGENT")
        self.logger.info("=" * 80)

        self.logger.info("Question Type : %s", type(question))
        self.logger.info("Question : %s", question)

        if not isinstance(question, str):
            raise TypeError(
                f"StockAgent expected question as str but received {type(question)}"
            )

        try:

            self.logger.info("Invoking LangGraph...")

            response = self.invoke_graph(question)

            self.logger.info("StockAgent completed successfully.")

            return response

        except Exception:

            self.logger.exception("StockAgent failed.")

            raise