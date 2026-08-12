"""
==============================================================================
Confidence Engine
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Calculates recommendation confidence based on agreement among
Technical, Fundamental, Sentiment and News analyzers.

==============================================================================
"""

from ai.recommendation.recommendation_models import (
    TechnicalResult,
    FundamentalResult,
    SentimentResult,
    NewsResult,
)


class ConfidenceEngine:
    """
    Calculates confidence in the final recommendation.
    """

    def calculate(
        self,
        technical: TechnicalResult,
        fundamental: FundamentalResult,
        sentiment: SentimentResult,
        news: NewsResult,
    ) -> tuple[float, str]:

        scores = [

            technical.score,

            fundamental.score,

            sentiment.score,

            news.score,

        ]

        average = sum(scores) / len(scores)

        deviation = sum(

            abs(score - average)

            for score in scores

        ) / len(scores)

        confidence = max(

            0.0,

            min(1.0, 1 - (deviation / 5))

        )

        if confidence >= 0.85:

            level = "Very High"

        elif confidence >= 0.70:

            level = "High"

        elif confidence >= 0.55:

            level = "Medium"

        else:

            level = "Low"

        return round(confidence, 2), level