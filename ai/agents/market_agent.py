"""
==============================================================================
Market AI Agent
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
AI Agent responsible for handling market-related queries.

Examples
--------
- How is NIFTY 50 performing today?
- Explain today's market movement.
- Which sector performed best?
- Market sentiment overview.

==============================================================================
"""

from ai.agents.base_agent import BaseAgent


class MarketAgent(BaseAgent):
    """
    AI Agent for handling market-related queries.
    """

    def run(self, question: str) -> str:
        """
        Process a market-related question.

        Parameters
        ----------
        question : str
            User question.

        Returns
        -------
        str
            AI generated response.
        """

        self.logger.info("MarketAgent processing request.")

        return self.invoke_graph(question)