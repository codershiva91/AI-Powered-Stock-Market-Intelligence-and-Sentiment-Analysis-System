"""
==============================================================================
Recommendation Node
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
LangGraph node responsible for generating AI-powered investment
recommendations.

Responsibilities
----------------
1. Read structured financial data from GraphState
2. Invoke Recommendation Engine
3. Store RecommendationResult in GraphState
4. Handle exceptions
5. Log execution details

==============================================================================
"""

from ai.common.logger import get_logger
from ai.langgraph.state import GraphState

from ai.recommendation.recommendation_engine import RecommendationEngine

logger = get_logger(__name__)


class RecommendationNode:
    """
    LangGraph node responsible for generating
    investment recommendations.
    """

    ######################################################################

    def __init__(self):

        self.engine = RecommendationEngine()

    ######################################################################

    def __call__(self, state: GraphState) -> GraphState:

        logger.info("=" * 60)
        logger.info("RECOMMENDATION NODE")
        logger.info("=" * 60)

        try:

            # ==========================================================
            # Read Graph State
            # ==========================================================

            stock_data = state.get("stock_data", {})

            technical_data = state.get("technical_data", {})

            fundamental_data = state.get("fundamental_data", {})

            sentiment_data = state.get("sentiment_data", {})

            news_documents = state.get("reranked_documents", [])

            logger.info(
                "Generating recommendation using "
                "Technical + Fundamental + Sentiment + News analysis."
            )

            # ==========================================================
            # Generate Recommendation
            # ==========================================================

            recommendation = self.engine.generate(

                stock_data=stock_data,

                technical_data=technical_data,

                fundamental_data=fundamental_data,

                sentiment_data=sentiment_data,

                news_documents=news_documents,

            )

            # ==========================================================
            # Save Recommendation
            # ==========================================================

            state["recommendation"] = {

                "recommendation": recommendation.recommendation,

                "confidence": recommendation.confidence,

                "total_score": recommendation.total_score,

                "technical_score": recommendation.technical_score,

                "fundamental_score": recommendation.fundamental_score,

                "sentiment_score": recommendation.sentiment_score,

                "news_score": recommendation.news_score,

                # Future Enhancement
                # "risk_score": recommendation.risk_score,

                "reasons": recommendation.reasons,

                "risks": recommendation.risks,

            }

            state["error"] = None

            logger.info(
                "Recommendation generated successfully: %s",
                recommendation.recommendation
            )

            return state

        except Exception as e:

            logger.exception("Recommendation Node failed.")

            state["recommendation"] = {}

            state["error"] = str(e)

            return state