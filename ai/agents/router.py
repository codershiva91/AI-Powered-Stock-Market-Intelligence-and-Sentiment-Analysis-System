"""
==============================================================================
AI Agent Router
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Routes the user's query to the appropriate AI Agent based on intent.

Supported Agents
----------------
1. News Agent
2. Stock Agent
3. Market Agent
4. Portfolio Agent

==============================================================================
"""

from enum import Enum
from typing import Dict, List

from ai.common.logger import get_logger

logger = get_logger(__name__)


# =============================================================================
# Agent Types
# =============================================================================

class AgentType(Enum):
    """
    Supported AI Agents.
    """

    NEWS = "news"
    STOCK = "stock"
    MARKET = "market"
    PORTFOLIO = "portfolio"


# =============================================================================
# Router
# =============================================================================

class Router:
    """
    Routes user queries to the appropriate AI agent.
    """

    def __init__(self):

        self.routes: Dict[AgentType, List[str]] = {

            AgentType.NEWS: [

                "news",
                "headline",
                "article",
                "announcement",
                "media",
                "press",
                "latest news",
            ],

            AgentType.STOCK: [

                "stock",
                "share",
                "price",
                "company",
                "fundamental",
                "technical",
                "indicator",
                "moving average",
                "rsi_14",
                "macd",
                "pe ratio",
                "eps",
            ],

            AgentType.MARKET: [

                "market",
                "nifty",
                "sensex",
                "sector",
                "economy",
                "index",
                "market sentiment",
            ],

            AgentType.PORTFOLIO: [

                "portfolio",
                "investment",
                "holdings",
                "risk",
                "allocation",
                "diversification",
            ]
        }

        logger.info("Router initialized successfully.")

    # -------------------------------------------------------------------------

    def route(self, question: str) -> AgentType:
        """
        Determine which agent should answer the question.

        Parameters
        ----------
        question : str

        Returns
        -------
        AgentType
        """

        if not question:
            logger.warning("Received empty question.")
            return AgentType.NEWS

        query = question.lower()

        logger.info(f"Routing question: {question}")

        for agent, keywords in self.routes.items():

            if any(keyword in query for keyword in keywords):

                logger.info(f"Selected Agent: {agent.value}")

                return agent

        logger.info("No matching keywords found. Defaulting to News Agent.")

        return AgentType.NEWS