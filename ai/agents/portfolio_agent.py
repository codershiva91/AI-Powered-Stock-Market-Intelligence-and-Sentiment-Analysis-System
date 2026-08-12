"""
==============================================================================
Portfolio AI Agent
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
AI Agent responsible for handling portfolio-related queries.

Examples
--------
- Analyse my portfolio.
- Suggest portfolio improvements.
- Evaluate portfolio risk.
- Diversification analysis.

==============================================================================
"""

from ai.agents.base_agent import BaseAgent


class PortfolioAgent(BaseAgent):
    """
    AI Agent for handling portfolio-related queries.
    """

    def run(self, question: str) -> str:
        """
        Process a portfolio-related question.

        Parameters
        ----------
        question : str
            User question.

        Returns
        -------
        str
            AI generated response.
        """

        self.logger.info("PortfolioAgent processing request.")

        return self.invoke_graph(question)