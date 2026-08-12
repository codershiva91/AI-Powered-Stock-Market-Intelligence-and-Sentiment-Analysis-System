"""
==============================================================================
Scoring Engine
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Combines Technical, Fundamental, Sentiment, News and Risk analysis
to generate the final investment recommendation.

Formula
-------

Final Score =
    (Technical × Technical Weight)
  + (Fundamental × Fundamental Weight)
  + (Sentiment × Sentiment Weight)
  + (News × News Weight)
  - (Risk × Risk Penalty Weight)

Returns
-------
RecommendationResult

==============================================================================
"""

from ai.recommendation.constants import (
    TECHNICAL_WEIGHT,
    FUNDAMENTAL_WEIGHT,
    SENTIMENT_WEIGHT,
    NEWS_WEIGHT,
    RISK_PENALTY_WEIGHT,
    BUY_THRESHOLD,
    HOLD_THRESHOLD,
)

from ai.recommendation.recommendation_models import (
    TechnicalResult,
    FundamentalResult,
    SentimentResult,
    NewsResult,
    RiskResult,
    RecommendationResult,
)

from ai.recommendation.confidence_engine import ConfidenceEngine


class ScoringEngine:
    """
    Combines analyzer outputs into a final investment recommendation.
    """

    def __init__(self):

        self.confidence_engine = ConfidenceEngine()

    ######################################################################

    def calculate(
        self,
        technical: TechnicalResult,
        fundamental: FundamentalResult,
        sentiment: SentimentResult,
        news: NewsResult,
        risk: RiskResult,
    ) -> RecommendationResult:

        result = RecommendationResult()

        # ==========================================================
        # Weighted Scores
        # ==========================================================

        weighted_technical = (
            technical.score * TECHNICAL_WEIGHT
        )

        weighted_fundamental = (
            fundamental.score * FUNDAMENTAL_WEIGHT
        )

        weighted_sentiment = (
            sentiment.score * SENTIMENT_WEIGHT
        )

        weighted_news = (
            news.score * NEWS_WEIGHT
        )

        risk_penalty = (
            risk.score * RISK_PENALTY_WEIGHT
        )

        total_score = (
            weighted_technical
            + weighted_fundamental
            + weighted_sentiment
            + weighted_news
            - risk_penalty
        )

        # Clamp score to range 0-10

        total_score = max(0.0, min(10.0, total_score))

        # ==========================================================
        # Recommendation
        # ==========================================================

        if total_score >= 8.5:

            recommendation = "STRONG BUY"

        elif total_score >= BUY_THRESHOLD:

            recommendation = "BUY"

        elif total_score >= HOLD_THRESHOLD:

            recommendation = "HOLD"

        elif total_score >= 3.0:

            recommendation = "SELL"

        else:

            recommendation = "STRONG SELL"

        # ==========================================================
        # Confidence
        # ==========================================================

        confidence, confidence_level = (
            self.confidence_engine.calculate(
                technical=technical,
                fundamental=fundamental,
                sentiment=sentiment,
                news=news,
            )
        )

        # ==========================================================
        # Populate Result
        # ==========================================================

        result.recommendation = recommendation

        result.confidence = confidence

        result.confidence_level = confidence_level

        result.total_score = round(total_score, 2)

        result.technical_score = round(
            technical.score,
            2,
        )

        result.fundamental_score = round(
            fundamental.score,
            2,
        )

        result.sentiment_score = round(
            sentiment.score,
            2,
        )

        result.news_score = round(
            news.score,
            2,
        )

        result.risk_score = round(
            risk.score,
            2,
        )

        # ==========================================================
        # Explainability
        # ==========================================================

        result.reasons.extend(technical.reasons)
        result.reasons.extend(fundamental.reasons)
        result.reasons.extend(sentiment.reasons)
        result.reasons.extend(news.reasons)

        result.risks.extend(technical.risks)
        result.risks.extend(fundamental.risks)
        result.risks.extend(sentiment.risks)
        result.risks.extend(risk.risks)

        # Remove duplicate entries while preserving order

        result.reasons = list(dict.fromkeys(result.reasons))

        result.risks = list(dict.fromkeys(result.risks))

        result.supporting_evidence = result.reasons.copy()

        return result