"""
==============================================================================
Recommendation Engine
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Coordinates all recommendation analyzers and generates the final
AI-powered investment recommendation.

Flow
----
Stock Data
      │
      ▼
Technical Analyzer
      │
      ▼
Fundamental Analyzer
      │
      ▼
Sentiment Analyzer
      │
      ▼
News Analyzer
      │
      ▼
Risk Analyzer
      │
      ▼
Scoring Engine
      │
      ▼
RecommendationResult

==============================================================================
"""

import time

from ai.common.logger import get_logger

from ai.recommendation.technical_analyzer import TechnicalAnalyzer
from ai.recommendation.fundamental_analyzer import FundamentalAnalyzer
from ai.recommendation.sentiment_analyzer import SentimentAnalyzer
from ai.recommendation.news_analyzer import NewsAnalyzer
from ai.recommendation.risk_analyzer import RiskAnalyzer
from ai.recommendation.scoring_engine import ScoringEngine

from ai.recommendation.recommendation_models import RecommendationResult

logger = get_logger(__name__)


class RecommendationEngine:
    """
    Coordinates all analyzers and generates the final investment recommendation.
    """

    ##################################################################

    def __init__(
        self,
        technical_analyzer=None,
        fundamental_analyzer=None,
        sentiment_analyzer=None,
        news_analyzer=None,
        risk_analyzer=None,
        scoring_engine=None,
    ):

        logger.info("Initializing Recommendation Engine...")

        self.technical_analyzer = technical_analyzer or TechnicalAnalyzer()

        self.fundamental_analyzer = (
            fundamental_analyzer or FundamentalAnalyzer()
        )

        self.sentiment_analyzer = (
            sentiment_analyzer or SentimentAnalyzer()
        )

        self.news_analyzer = news_analyzer or NewsAnalyzer()

        self.risk_analyzer = risk_analyzer or RiskAnalyzer()

        self.scoring_engine = scoring_engine or ScoringEngine()

    ##################################################################

    def generate(
        self,
        stock_data: dict | None,
        technical_data: dict | None,
        fundamental_data: dict | None,
        sentiment_data: dict | None,
        news_documents: list[dict] | None,
    ) -> RecommendationResult:
        """
        Generate the final investment recommendation.
        """

        logger.info("=" * 60)
        logger.info("RECOMMENDATION ENGINE")
        logger.info("=" * 60)

        start_time = time.perf_counter()

        # ------------------------------------------------------------------
        # Defensive Defaults
        # ------------------------------------------------------------------

        stock_data = stock_data or {}
        technical_data = technical_data or {}
        fundamental_data = fundamental_data or {}
        sentiment_data = sentiment_data or {}
        news_documents = news_documents or []

        try:

            ##################################################################
            # Technical Analysis
            ##################################################################

            technical_result = self.technical_analyzer.analyze(
                stock_data=stock_data,
                technical_data=technical_data,
            )

            ##################################################################
            # Fundamental Analysis
            ##################################################################

            fundamental_result = self.fundamental_analyzer.analyze(
                fundamental_data=fundamental_data
            )

            ##################################################################
            # Sentiment Analysis
            ##################################################################

            sentiment_result = self.sentiment_analyzer.analyze(
                sentiment_data=sentiment_data
            )

            ##################################################################
            # News Analysis
            ##################################################################

            news_result = self.news_analyzer.analyze(
                documents=news_documents
            )

            ##################################################################
            # Risk Analysis
            ##################################################################

            risk_result = self.risk_analyzer.analyze(
                technical_data=technical_data,
                fundamental_data=fundamental_data,
                sentiment_data=sentiment_data,
                news_result=news_result,
            )

            ##################################################################
            # Final Recommendation
            ##################################################################

            recommendation = self.scoring_engine.calculate(
                technical=technical_result,
                fundamental=fundamental_result,
                sentiment=sentiment_result,
                news=news_result,
                risk=risk_result,
            )

            elapsed = time.perf_counter() - start_time

            logger.info(
                "Recommendation=%s | Score=%.2f | Confidence=%.2f | Time=%.3fs",
                recommendation.recommendation,
                recommendation.total_score,
                recommendation.confidence,
                elapsed,
            )

            logger.info("Recommendation generated successfully.")

            return recommendation

        except Exception as e:

            logger.exception(
                "Recommendation Engine failed: %s",
                str(e),
            )

            raise