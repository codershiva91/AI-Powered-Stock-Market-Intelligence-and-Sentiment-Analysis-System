"""
==============================================================================
Sentiment Analyzer
==============================================================================

Author      : Shivam Sahu
Project     : AI-Driven Stock Market Intelligence System

Description
-----------
Evaluates company news sentiment using FinBERT sentiment scores.

The analyzer converts aggregated sentiment information into
a sentiment score that contributes to the final recommendation.

Returns
-------
SentimentResult

==============================================================================
"""

from ai.recommendation.recommendation_models import SentimentResult


class SentimentAnalyzer:
    """
    Performs sentiment analysis using aggregated FinBERT results.
    """

    def analyze(self, sentiment_data: dict) -> SentimentResult:

        result = SentimentResult()

        if not sentiment_data:

            result.risks.append(
                "News sentiment data is unavailable."
            )

            return result

        score = 0.0

        # ------------------------------------------------------------
        # Read Aggregated Sentiment
        # ------------------------------------------------------------

        overall_sentiment = sentiment_data.get(
            "overall_sentiment",
            "Neutral"
        )

        confidence = sentiment_data.get(
            "confidence",
            0.0
        )

        positive_count = sentiment_data.get(
            "positive_count",
            0
        )

        neutral_count = sentiment_data.get(
            "neutral_count",
            0
        )

        negative_count = sentiment_data.get(
            "negative_count",
            0
        )

        # ------------------------------------------------------------
        # Overall Sentiment
        # ------------------------------------------------------------

        if overall_sentiment == "Positive":

            score += 2

            result.reasons.append(
                "Overall market sentiment is Positive."
            )

        elif overall_sentiment == "Negative":

            score -= 2

            result.risks.append(
                "Overall market sentiment is Negative."
            )

        else:

            result.reasons.append(
                "Overall market sentiment is Neutral."
            )

        # ------------------------------------------------------------
        # Confidence
        # ------------------------------------------------------------

        if confidence >= 0.90:

            score += 1

            result.reasons.append(
                f"High sentiment confidence ({confidence:.2%})."
            )

        elif confidence < 0.60:

            score -= 1

            result.risks.append(
                f"Low sentiment confidence ({confidence:.2%})."
            )

        # ------------------------------------------------------------
        # Positive vs Negative News
        # ------------------------------------------------------------

        if positive_count > negative_count:

            score += 1

            result.reasons.append(
                "Positive news outweighs negative news."
            )

        elif negative_count > positive_count:

            score -= 1

            result.risks.append(
                "Negative news outweighs positive news."
            )

        # ------------------------------------------------------------
        # Save Results
        # ------------------------------------------------------------

        result.score = score
        result.overall_sentiment = overall_sentiment
        result.confidence = confidence

        return result