"""
==============================================================================
AI Supervisor
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Main entry point for the AI Agent Layer.

Responsibilities
----------------
1. Receive user question
2. Route question to the appropriate AI Agent
3. Execute the selected agent
4. Return final response

Workflow
--------
User
 │
 ▼
Supervisor
 │
 ▼
Router
 │
 ▼
Agent
 │
 ▼
LangGraph
 │
 ▼
Response

==============================================================================
"""

from typing import Dict

from ai.common.logger import get_logger
from ai.common.exceptions import AgentError

from ai.agents.router import Router, AgentType
from ai.agents.news_agent import NewsAgent
from ai.agents.stock_agent import StockAgent
from ai.agents.market_agent import MarketAgent
from ai.agents.portfolio_agent import PortfolioAgent


logger = get_logger(__name__)


class Supervisor:
    """
    Main Supervisor for the AI Agent Layer.
    """

    def __init__(self) -> None:

        logger.info("Initializing AI Supervisor...")

        self.router = Router()

        # Agent Registry
        self.agents: Dict[AgentType, object] = {

            AgentType.NEWS: NewsAgent(),

            AgentType.STOCK: StockAgent(),

            AgentType.MARKET: MarketAgent(),

            AgentType.PORTFOLIO: PortfolioAgent(),

        }

        logger.info("AI Supervisor initialized successfully.")

    # ------------------------------------------------------------------

    def handle(self, question: str) -> str:
        """
        Handle a user question.

        Parameters
        ----------
        question : str

        Returns
        -------
        str
        """

        logger.info(f"Received Question: {question}")

        try:

            agent_type = self.router.route(question)

            logger.info(f"Selected Agent: {agent_type.value}")

            agent = self.agents.get(agent_type)

            if agent is None:
                raise AgentError(
                    f"No agent registered for {agent_type.value}"
                )

            return agent.run(question)

        except Exception as e:

            logger.exception("Supervisor execution failed.")

            raise AgentError(
                f"Supervisor Error: {str(e)}"
            ) from e